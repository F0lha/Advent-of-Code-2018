
with open("../inputs/day5-1.txt") as file:
    for line in file:
        polymer = list(line[:-1])

idx = 0
while idx < len(polymer) - 1:
    prev = polymer[idx]
    after = polymer[idx + 1]
    if prev.lower() == after.lower() and prev != after:
        polymer.pop(idx) # removes prev
        polymer.pop(idx) # removes after
        idx -= 1
        if idx < 0:
            idx = 0
        continue
    else:
        idx += 1

print(len(polymer))
