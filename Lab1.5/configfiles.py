from glob import glob as glob


confs = glob("*.txt")
l = []

for f in confs:
    with open(f) as file:
        for s in file:
            if "ip address" in s:
                l.append(s)

l = sorted(list(set(l)))
i=0
while i < 5:
    l.pop()
    i=i+1

for i in l:
    i = i.replace("ip address", "")
    print(i)
