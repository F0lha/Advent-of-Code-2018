import re
cloth = {}
with open("../inputs/day3-1.txt") as file:
    for line in file:
        info = re.split('#|@|:', line[:-1])[1:]
        #ignore claim ID
        start = info[1].split(",")
        x1 = int(start[0])
        y1 = int(start[1])
        size = info[2].split("x")
        w = int(size[0])
        h = int(size[1])
        for i in range(x1, x1 + w):
            for j in range(y1, y1 + h):
                if str(i)+"/"+str(j) not in cloth.keys():
                    cloth[str(i)+"/"+str(j)] = 1
                else:
                    cloth[str(i)+"/"+str(j)] += 1
        
count = 0
for key, value in cloth.items():
    if value > 1:
        count += 1
print(count)