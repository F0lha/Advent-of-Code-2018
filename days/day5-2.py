with open("../inputs/day5-1.txt") as file:
    for line in file:
        polymer = list(line[:-1])

lower_poly = [x.lower() for x in polymer]
diff = len(set(lower_poly))

first = ord('a')

best_length = float('inf')
for i in range(diff):
    char_to_del = chr(first+i)
    current_poly = [x for x in polymer if x.lower() != char_to_del]
    idx = 0
    while idx < len(current_poly) - 1:
        prev = current_poly[idx]
        after = current_poly[idx + 1]
        if prev.lower() == after.lower() and prev != after:
            current_poly.pop(idx) # removes prev
            current_poly.pop(idx) # removes after
            idx -= 1
            if idx < 0:
                idx = 0
            continue
        else:
            idx += 1

    best_length = len(current_poly) if len(current_poly) < best_length else best_length
        
print(best_length)