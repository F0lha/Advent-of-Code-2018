import random
import itertools
from collections import Counter

def datadiff(date1, date2):
    minutes1, minutes2 = date1[-2:], date2[-2:]  # no need for other things because they only fall asleep during this time
    return range(int(minutes1), int(minutes2))


#order events
events = list()
with open("../inputs/day4-1.txt") as file:
    for line in file:
        date = line[1:17]
        event = line[19:-1]
        events += [(date, event)]
    
events = sorted(events, key=lambda x: x[0])

guards = {}
summation = []
current_guard = None

for event in events:
    if event[1][0] == "G":
        if current_guard is not None:
            if current_guard in guards.keys():
                guards[current_guard] += summation
            else:
                guards[current_guard] = summation
        current_guard = event[1].split("#")[1].split(" ")[0]
        summation = []
    elif event[1][0] == "f":
        prev = event[0]
    else:
        summation += datadiff(prev, event[0])

max_sleep = 0
max_guard = None
max_minutes = None
for key, value in guards.items():
    if len(value) > max_sleep:
        max_sleep = len(value)
        max_guard = key
        max_minutes = value

minute = Counter(max_minutes).most_common(1)[0][0]

print(int(max_guard)*minute)