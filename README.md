# Competitive Programming

Repositório com minhas soluções de problemas de programação competitiva, principalmente do Codeforces, e alguns templates que uso pra consultar rápido durante as provas.

## Estrutura

Os problemas ficam organizados por faixa de rating:

```text
meu-repo/
├── exercises/
│   ├── 800-1200/
│   ├── 1200-1600/
│   ├── 1600+/
│   └── misc/
│
├── notebook/
│   └── topics/
│       ├── 00_entrada_saida.py
│       ├── 01_estruturas_dados.py
│       ├── 02_matematica.py
│       ├── 03_progressoes.py
│       ├── 04_combinatoria.py
│       ├── 05_geometria.py
│       ├── 06_guloso.py
│       ├── 07_backtracking.py
│       ├── 08_dp.py
│       ├── 09_grafos.py
│       ├── 10_dijkstra.py
│       ├── 11_dsu.py
│       ├── 12_kruskal.py
│       ├── 13_topologico.py
│       └── 14_jogos.py
│
├── scripts/
│   └── progress.py
│
├── progress.png
└── README.md
```

## Templates

Em `notebook/topics` estão os templates que uso com mais frequência:

- [`00_entrada_saida.py`](notebook/topics/00_entrada_saida.py) — entrada e saída rápida
- [`01_estruturas_dados.py`](notebook/topics/01_estruturas_dados.py) — estruturas de dados
- [`02_matematica.py`](notebook/topics/02_matematica.py) — matemática básica
- [`03_progressoes.py`](notebook/topics/03_progressoes.py) — progressões
- [`04_combinatoria.py`](notebook/topics/04_combinatoria.py) — combinatória
- [`05_geometria.py`](notebook/topics/05_geometria.py) — geometria computacional
- [`06_guloso.py`](notebook/topics/06_guloso.py) — algoritmos gulosos
- [`07_backtracking.py`](notebook/topics/07_backtracking.py) — backtracking
- [`08_dp.py`](notebook/topics/08_dp.py) — programação dinâmica
- [`09_grafos.py`](notebook/topics/09_grafos.py) — DFS e BFS
- [`10_dijkstra.py`](notebook/topics/10_dijkstra.py) — menor caminho
- [`11_dsu.py`](notebook/topics/11_dsu.py) — union-find (DSU)
- [`12_kruskal.py`](notebook/topics/12_kruskal.py) — árvore geradora mínima
- [`13_topologico.py`](notebook/topics/13_topologico.py) — ordenação topológica
- [`14_jogos.py`](notebook/topics/14_jogos.py) — teoria dos jogos

## Progresso

O gráfico abaixo é atualizado automaticamente e mostra quantos problemas eu já resolvi em cada faixa de rating:

<p align="center">
  <img src="progress.png" width="650">
</p>

| Rating | Nível |
|--------|-------|
| 800–1200 | Básico |
| 1200–1600 | Intermediário |
| 1600+ | Avançado |

Um script em `scripts/progress.py` conta as soluções em cada pasta, gera o gráfico com Matplotlib e atualiza a imagem via GitHub Actions toda vez que um novo problema é adicionado.

## Objetivo

Manter uma rotina de treino em CP, guardar os templates que uso de verdade (em vez de reescrever tudo do zero cada prova) e ter um jeito visual de acompanhar minha evolução por nível de dificuldade.

## Tecnologias

Python, Matplotlib e GitHub Actions.

---

Thalles Saraiva
