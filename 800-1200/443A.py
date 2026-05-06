s = input().strip("{}").split(", ")
semCopias = list(set(s))
if len(semCopias) == 1 and semCopias[0] == "":
    print(0)
else:
    print(len(semCopias))