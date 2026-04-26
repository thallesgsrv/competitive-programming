def main():
    num = int(input())
    cont = 0
    while num > 0:
        num &= (num-1)
        cont += 1
    print(cont)
main()
