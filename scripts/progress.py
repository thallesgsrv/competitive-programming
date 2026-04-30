import os
import re
import shutil
import json
import sys
from pathlib import Path
from time import sleep
import matplotlib.pyplot as plt

# ==================== CONFIGURAÇÕES ====================
SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent

# Detectar se está rodando no GitHub Actions
IS_GITHUB_ACTIONS = os.environ.get('GITHUB_ACTIONS') == 'true'

DEFAULT_RATING = 1000

# Pastas do Codeforces (com rating)
RATING_PASTAS = {
    "800-1200": (800, 1200),
    "1200-1600": (1200, 1600),
    "1600+": (1600, 5000)
}

# Pasta para tudo que não é Codeforces ou não tem rating
PASTA_MISC = "misc"

CACHE_FILE = SCRIPT_DIR / "problems_cache.json"
# ======================================================

def is_codeforces_file(nome):
    """Verifica se o nome do arquivo parece ser do Codeforces (tem ID como 4A, 158A, etc.)"""
    match = re.match(r'^(\d+[A-Z]\d*)', nome)
    if not match:
        match = re.match(r'^(\d+[A-Z])', nome)
    if not match:
        match = re.match(r'^([A-Z]\d*)', nome)
    return match is not None

def extract_codeforces_id(nome):
    """Extrai o ID do Codeforces do nome do arquivo"""
    match = re.match(r'(\d+[A-Z]\d*)', nome)
    if not match:
        match = re.match(r'(\d+[A-Z])', nome)
    if not match:
        match = re.match(r'^([A-Z]\d*)', nome)
    return match.group(1) if match else None

def get_problem_rating(problem_id):
    """Busca o rating de um problema do Codeforces"""
    match = re.match(r'(\d+)([A-Z]\d*)', problem_id)
    if not match:
        match = re.match(r'([A-Z]\d*)', problem_id)
        if not match:
            return None

    contest_id = match.group(1)
    index = match.group(2) if len(match.groups()) > 1 else match.group(1)

    cache = {}
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r') as f:
                cache = json.load(f)
                key = f"{contest_id}{index}"
                if key in cache:
                    return cache[key]
        except:
            pass

    if IS_GITHUB_ACTIONS:
        return None

    try:
        print(f"  🔍 Buscando rating: {problem_id}...")
        import requests
        url = "https://codeforces.com/api/problemset.problems"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data['status'] == 'OK':
            for problem in data['result']['problems']:
                if str(problem.get('contestId')) == contest_id and problem.get('index') == index:
                    rating = problem.get('rating')

                    if rating is None:
                        rating = DEFAULT_RATING
                    else:
                        print(f"  ✅ {problem_id}: rating = {rating}")

                    cache_key = f"{contest_id}{index}"
                    cache[cache_key] = rating
                    with open(CACHE_FILE, 'w') as f:
                        json.dump(cache, f, indent=2)

                    sleep(0.3)
                    return rating
            return None
        return None
    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return None

def get_rating_folder(rating):
    for folder, (min_r, max_r) in RATING_PASTAS.items():
        if min_r <= rating < max_r:
            return folder
    return "1600+"

def organizar_arquivos():
    """Organiza arquivos: Codeforces com rating vai para pastas, resto vai para misc/"""
    if IS_GITHUB_ACTIONS:
        print("\n🤖 GitHub Actions: pulando organização (apenas geração de gráfico)")
        return None

    # Criar pastas necessárias
    for folder in RATING_PASTAS.keys():
        (BASE_DIR / folder).mkdir(exist_ok=True)
    (BASE_DIR / PASTA_MISC).mkdir(exist_ok=True)

    # Procurar arquivos .py na raiz (ignorar o próprio script)
    arquivos = [f for f in BASE_DIR.glob("*.py") if f.parent == BASE_DIR]
    arquivos = [f for f in arquivos if f.name not in ["progress.py"]]

    if not arquivos:
        print("\n📭 Nenhum arquivo .py encontrado!")
        return None

    print(f"\n📁 Encontrados {len(arquivos)} arquivos\n")

    stats = {
        "movidos": 0,
        "codeforces": 0,
        "misc": 0,
        "por_pasta": {folder: 0 for folder in RATING_PASTAS.keys()}
    }
    stats["por_pasta"][PASTA_MISC] = 0

    for arquivo in arquivos:
        nome = arquivo.stem
        print(f"\n📄 Processando: {nome}")

        # Verificar se é Codeforces (tem ID no formato)
        if is_codeforces_file(nome):
            problem_id = extract_codeforces_id(nome)
            print(f"  🔍 Identificado como Codeforces: ID = {problem_id}")
            rating = get_problem_rating(problem_id)

            if rating is not None:
                destino = get_rating_folder(rating)
                destino_path = BASE_DIR / destino / arquivo.name

                if not destino_path.exists():
                    shutil.move(str(arquivo), str(destino_path))
                    print(f"  📂 Movido para: {destino}/")
                    stats["movidos"] += 1
                    stats["codeforces"] += 1
                    stats["por_pasta"][destino] += 1
                else:
                    print(f"  ⚠️ Arquivo já existe em {destino}")
            else:
                # Codeforces sem rating vai para misc
                destino_path = BASE_DIR / PASTA_MISC / arquivo.name
                shutil.move(str(arquivo), str(destino_path))
                print(f"  📂 Movido para: {PASTA_MISC}/ (CF sem rating)")
                stats["movidos"] += 1
                stats["misc"] += 1
                stats["por_pasta"][PASTA_MISC] += 1
        else:
            # Não é Codeforces → misc
            destino_path = BASE_DIR / PASTA_MISC / arquivo.name
            shutil.move(str(arquivo), str(destino_path))
            print(f"  📂 Movido para: {PASTA_MISC}/")
            stats["movidos"] += 1
            stats["misc"] += 1
            stats["por_pasta"][PASTA_MISC] += 1

    return stats

def gerar_grafico():
    """Gera o gráfico de progresso (Codeforces por rating + misc)"""
    data = {}
    
    # Contar Codeforces por rating
    for folder in RATING_PASTAS.keys():
        folder_path = BASE_DIR / folder
        if folder_path.exists():
            data[folder] = len([x for x in folder_path.glob("*.py")])
        else:
            data[folder] = 0
    
    # Contar misc
    misc_path = BASE_DIR / PASTA_MISC
    if misc_path.exists():
        data[PASTA_MISC] = len([x for x in misc_path.glob("*.py")])
    else:
        data[PASTA_MISC] = 0

    # Remover pastas vazias
    data = {k: v for k, v in data.items() if v > 0}

    if not data:
        print("\n📊 Nenhum dado para exibir no gráfico!")
        return False

    cores = ['#ff6b6b', '#feca57', '#48dbfb', '#a0a0a0']

    plt.figure(figsize=(12, 6))

    barras = plt.bar(data.keys(), data.values(), color=cores[:len(data)],
                     edgecolor='black', linewidth=1.5)

    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura + 0.3,
                 f'{int(altura)}', ha='center', va='bottom',
                 fontsize=11, fontweight='bold')

    plt.title("🚀 Codeforces Progress", fontsize=16, fontweight='bold', pad=20)
    plt.xlabel("⭐ Dificuldade / Categoria", fontsize=12, fontweight='bold')
    plt.ylabel("📚 Problemas Resolvidos", fontsize=12, fontweight='bold')
    plt.grid(axis='y', alpha=0.3, linestyle='--')

    max_valor = max(data.values())
    plt.ylim(0, max_valor + max_valor * 0.2)

    plt.tight_layout()

    output_path = BASE_DIR / "progress.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n📊 Gráfico salvo: {output_path}")
    print(f"\n📈 Resumo:")
    for categoria, qtd in data.items():
        print(f"  {categoria}: {qtd} problemas")
    print(f"  Total: {sum(data.values())} problemas")

    return True

def mostrar_estatisticas(stats):
    if stats is None:
        return

    print("\n" + "="*50)
    print("📊 ESTATÍSTICAS DA ORGANIZAÇÃO")
    print("="*50)
    print(f"\n✅ Total movidos: {stats['movidos']}")
    print(f"  ├─ Codeforces com rating: {stats['codeforces']}")
    print(f"  └─ Misc (outros judges + CF sem rating): {stats['misc']}")

    print("\n📁 Distribuição final:")
    for pasta, count in stats['por_pasta'].items():
        if count > 0:
            print(f"  {pasta}: {count}")

def buscar_rating_manual():
    if IS_GITHUB_ACTIONS:
        return

    print("\n🔍 Buscar rating de problema do Codeforces")
    problem_id = input("Digite o ID (ex: 4A, 158A): ").strip()
    if problem_id:
        rating = get_problem_rating(problem_id)
        if rating:
            print(f"✅ Rating: {rating}")
            print(f"📂 Pasta: {get_rating_folder(rating)}")

def menu_principal():
    print(f"\n📂 Base: {BASE_DIR}")
    print(f"📁 Pasta misc: {PASTA_MISC}/ (outros judges + CF sem rating)")

    if IS_GITHUB_ACTIONS:
        print("\n🤖 GitHub Actions: gerando gráfico automaticamente...")
        gerar_grafico()
        return

    while True:
        print("\n" + "="*50)
        print("🎯 ORGANIZADOR DE PROBLEMAS")
        print("="*50)
        print("\n1️⃣  Organizar arquivos")
        print("2️⃣  Gerar gráfico")
        print("3️⃣  Buscar rating (Codeforces)")
        print("4️⃣  Sair")

        opcao = input("\n👉 Escolha (1-4): ").strip()

        if opcao == "1":
            confirmar = input("Mover arquivos? (s/n): ").lower()
            if confirmar == 's':
                stats = organizar_arquivos()
                mostrar_estatisticas(stats)
                if input("\nGerar gráfico? (s/n): ").lower() == 's':
                    gerar_grafico()
        elif opcao == "2":
            gerar_grafico()
        elif opcao == "3":
            buscar_rating_manual()
        elif opcao == "4":
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida")

if __name__ == "__main__":
    try:
        import matplotlib
    except ImportError:
        print("❌ Instale: pip install matplotlib")
        exit(1)

    menu_principal()