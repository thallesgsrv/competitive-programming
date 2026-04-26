import os
import matplotlib.pyplot as plt

BASE = "."

folders = ["800-1200", "1200-1600", "1600+"]

data = {}

for f in folders:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        data[f] = len([x for x in os.listdir(path) if x.endswith(".py")])
    else:
        data[f] = 0

plt.figure()
plt.bar(data.keys(), data.values())

plt.title("Codeforces Progress")
plt.xlabel("Rating")
plt.ylabel("Problems solved")

plt.savefig("progress.png")
