xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

ac = (xA - xC)**2 + (yA - yC)**2
ab = (xA - xB)**2 + (yA - yB)**2
bc = (xB - xC)**2 + (yB - yC)**2

if (ac + ab == bc) or (ab + bc == ac) or (ac + bc == ab):
    print("Yes")
else:
    print("No")