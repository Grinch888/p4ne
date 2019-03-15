from glob import glob as glob


confs = glob("*.txt")
l = []

for f in confs:
    with open(f) as file:
        for s in file:
            if "ip address" in s:
                if ("dhcp" not in s) and ("match" not in s) and ("no" not in s):
                    l.append(s)

l = sorted(list(set(l)))


for i in l:
    i = i.replace("ip address", "")
    print(i)
