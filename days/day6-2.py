from collections import Counter
pointsx = []
pointsy = []
limit = 10000
with open("../inputs/day6-1.txt") as file:
    for line in file:
        l = line.split(",")
        pointsx += [int(l[0])]
        pointsy += [int(l[1][1:])]

candidates = list(range(len(pointsx)))

grid = [[0 for _ in range(max(pointsy)+1)] for _ in range(max(pointsx)+1)]

for coord, (x, y) in enumerate(zip(pointsx, pointsy)):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += abs(x-i) + abs(y-j)
flat_grid = [item for sublist in grid for item in sublist]

flat_grid = [1 if x < limit else -1 for x in flat_grid]

print(flat_grid.count(1))