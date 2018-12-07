nodes = {}
node_set = set()

with open("../inputs/day7-1.txt") as file:
    for line in file:
        l = line.split(" ")
        first = l[1]
        second = l[-3]
        if second not in nodes.keys():
            nodes[second] = [first]
        else:
            nodes[second] += [first]

        node_set.add(first)
        node_set.add(second)


node_set = sorted(node_set)

answer = []
time = 0
offset = ord('A') 
workers = [[-1, None], [-1, None], [-1, None], [-1, None], [-1, None]]

def get_worker(workers):
    for i in range(len(workers)):
        if workers[i][0] <= 0:
            return i
    return -1

def update_workers(workers):
    global time
    time += 1
    for worker in workers:
        worker[0] -= 1

def busy_workers(workers):
    for worker in workers:
        if worker[0] >  0:
            return True

    return False

while len(node_set) > 0 or busy_workers(workers):
    #get a worker
    for i in range(len(workers)):
        if workers[i][1] is not None and workers[i][0] == 0:
            if workers[i][1] in nodes.keys():
                nodes.pop(workers[i][1])
            for key, value in nodes.items():
                if workers[i][1] in value:
                    value.remove(workers[i][1])

    #get available node
    curr_node = [x for x in node_set if x not in nodes.keys() or len(nodes[x]) == 0]

    for curr in curr_node:
        current_worker = get_worker(workers)
        if current_worker != -1:
            if curr != -1:
                node_set.remove(curr)
                workers[current_worker] = [60 + ord(curr) - offset + 1, curr]

    #work
    update_workers(workers)

print(time)
