summation = 0
with open("../inputs/day1-1.txt") as file:
    for line in file:
        summation += int(line)

print(summation)