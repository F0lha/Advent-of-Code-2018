from collections import Counter
pointsx = []
pointsy = []
with open("../inputs/day6-1.txt") as file:
    for line in file:
        l = line.split(",")
        pointsx += [int(l[0])]
        pointsy += [int(l[1][1:])]

candidates = list(range(len(pointsx)))

grid = [[(0, float('inf')) for _ in range(max(pointsy)+1)] for _ in range(max(pointsx)+1)]

for coord, (x, y) in enumerate(zip(pointsx, pointsy)):
    grid[x][y] = (-1, float('inf'))
    if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1:
        candidates.remove(coord)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curr_dist = abs(x-i) + abs(y-j)
            if curr_dist < grid[i][j][1] and grid[i][j][0] != -1:
                grid[i][j] = (coord, curr_dist)
            elif curr_dist == grid[i][j][1] and grid[i][j][0] != -1:
                grid[i][j] = (-2, curr_dist)
    
# elim margin 
for i in range(len(grid)):
    if grid[i][0][0] in candidates:
        candidates.remove(grid[i][0][0])
    if grid[i][-1][0] in candidates:
        candidates.remove(grid[i][-1][0])
            
        
for i in range(len(grid[0])):
    if grid[0][i][0] in candidates:
        candidates.remove(grid[0][i][0])
    if grid[-1][i][0] in candidates:
        candidates.remove(grid[-1][i][0])

flat_grid = [item for sublist in grid for item in sublist]

# leave only candidates

flat_grid = [x[0] if x[0] in candidates else -1 for x in flat_grid]

size = Counter(flat_grid).most_common()[1][1]

print(size+1) # the coordinate iteself