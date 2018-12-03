import re
cloth = {}
ids = []
with open("../inputs/day3-1.txt") as file:
    for line in file:
        info = re.split('#|@|:', line[:-1])[1:]
        #ignore claim ID
        ID = info[0]
        start = info[1].split(",")
        x1 = int(start[0])
        y1 = int(start[1])
        size = info[2].split("x")
        w = int(size[0])
        h = int(size[1])
        for i in range(x1, x1 + w):
            for j in range(y1, y1 + h):
                if str(i)+"/"+str(j) not in cloth.keys():
                    cloth[str(i)+"/"+str(j)] = [-1, []]
                    cloth[str(i)+"/"+str(j)][0] = 1
                    cloth[str(i)+"/"+str(j)][1] = [ID]
                else:
                    cloth[str(i)+"/"+str(j)][0] += 1
                    if ID not in cloth[str(i)+"/"+str(j)][1]:
                        cloth[str(i)+"/"+str(j)][1] += [ID]
        ids += [ID]


count = 0
for key, value in cloth.items():
    if value[0] > 1:
        for id in value[1]:
            if id in ids:
                ids.remove(id)

print(ids)