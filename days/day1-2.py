# super greedy
summation = 0
l = [0]
found = False
while not found:
    with open("../inputs/day1-1.txt") as file:
        for line in file:
            summation += int(line)
            if summation in l:
                print(summation)
                found = True
                break
            else:
                l += [summation]
        print(summation)
        break
        if found:
            break