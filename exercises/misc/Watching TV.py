for _ in range(int(input())):
    dict = {}
    for _ in range(int(input())):
        s, f = input().split()
        if f in dict:
            dict[f] += 1
        else:
            dict[f] = +1
    big = 0
    freq = 0
    for elem in dict.items():
        if elem[1] > big:
            big = elem[1]
            freq = elem[0]
        if elem[1] == big:
            freq = min(freq, elem[0])
    print(freq)
