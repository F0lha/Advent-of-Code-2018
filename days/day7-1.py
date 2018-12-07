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

while len(node_set) > 0:
    curr_node = [x for x in node_set if x not in nodes.keys() or len(nodes[x]) == 0][0]
    answer += [curr_node]
    node_set.remove(curr_node)
    if curr_node in nodes.keys():
        nodes.pop(curr_node)
    for key, value in nodes.items():
        if curr_node in value:
            value.remove(curr_node)

print("".join(answer))
