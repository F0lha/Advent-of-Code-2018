file = []
with open("../inputs/day2-1.txt") as _file:
    for line in _file:
        file += [line[:-1]]
        
found = False
for i in range(len(file)):
    for j in range(i+1, len(file)):
        diff = 0
        #compare each letter (possible to compare string at once maybe)
        for l1, l2 in zip(file[i], file[j]):
            diff += 1 if int(ord(l1) - ord(l2)) != 0 else 0

        if diff == 1:
            found = True
            break
    if found:
        break
# lazy
print(file[i])
print(file[j])