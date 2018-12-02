repeats = {}
with open("../inputs/day2-1.txt") as file:
    for line in file:
        line_repeats = {}
        for letter in line:
            if letter in line_repeats.keys():
                line_repeats[letter] += 1
            else:
                line_repeats[letter] = 1
        values_used = []
        for key, value in line_repeats.items():
            if value > 1 and value not in values_used:
                if value in repeats.keys():
                    repeats[value] += 1
                else:
                    repeats[value] = 1
                values_used += [value]

result = 1
for _, value in repeats.items():
    result *= value

print(result)
