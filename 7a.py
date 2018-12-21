import re

with open("7.txt", "r") as f:
    reg = re.compile('[A-Z]\\W')
    graph = dict()
    conditions = dict()
    for line in f.readlines():
        k, v = map(str.rstrip, reg.findall(line))
        if k not in graph.keys():
            graph[k] = set(v)
        else:
            graph[k].add(v)
        
        if v not in conditions.keys():
            conditions[v] = set(k)
        else:
            conditions[v].add(k)


    start = list(graph.keys() - conditions.keys())
    end = list(conditions.keys() - graph.keys()).pop()

    start.sort()

    current, *nextAvailable = start
    order = []

    def isConditionsFullfilled(node):
        if node not in conditions.keys():
            return True
        else:
            return conditions[node].issubset(set(order))

    while not conditions[end].issubset(set(order)):
        if isConditionsFullfilled(current):
            order.append(current)
            if current in graph.keys():
                nextAvailable.extend(graph[current])
                nextAvailable = list(set(nextAvailable))
                nextAvailable.sort()
                current, *nextAvailable = nextAvailable
        else:
            nextAvailable.append(current)
            current, *nextAvailable = nextAvailable


    order.append(end)
    
    print("".join(order))