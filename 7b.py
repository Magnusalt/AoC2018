import re
import string


class Worker:
    def __init__(self, offsetStart, workItem):
        self.finishTime = offsetStart + self.letterToSeconds(workItem)
        self.workItem = workItem

    def letterToSeconds(self, l):
        return string.ascii_uppercase.index(l) + 60


class WorkerPool:
    def __init__(self, maxNumberOfWorkers):
        self.maxNumberOfWorkers = maxNumberOfWorkers
        self.workers = []

    def hasFreeWorkers(self):
        return len(self.workers) < self.maxNumberOfWorkers

    def assignWorker(self, offsetStart, workItem):
        if self.hasFreeWorkers():
            self.workers.append(Worker(offsetStart, workItem))
            return True
        return False

    def update(self, currentTime):
        workersToRemove = []
        for w in self.workers:
            if w.finishTime == currentTime:
                workersToRemove.append(w)
        for w in workersToRemove:
            self.workers.remove(w)
        return list(map(lambda w: w.workItem, workersToRemove))
    
    def isBeingProcessed(self, workItem):
        for w in self.workers:
            if w.workItem == workItem:
                return True
        return False
    
    def getNumberOfFreeWorkers(self):
        return list(map(lambda w: w.workItem, self.workers))


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

    order = []

    workerpool = WorkerPool(5)
    for wi in start:
        workerpool.assignWorker(0, wi)

    sec = 0
    nextAvailable = []

    def isConditionsFullfilled(node):
        if node not in conditions.keys():
            return True
        else:
            return conditions[node].issubset(set(order))

    while end not in order:
        workitemsJustFinished = workerpool.update(sec)
        print(sec, "".join(order), workitemsJustFinished, workerpool.getNumberOfFreeWorkers())
        for wi in workitemsJustFinished:
            if wi in graph.keys():
                order.append(wi)
                newItemsToProcess = graph[wi]
                for i in newItemsToProcess:
                    if not workerpool.isBeingProcessed(i) and i not in order:
                        nextAvailable.append(i)
                nextAvailable = list(set(nextAvailable))
                nextAvailable.sort()
                print(nextAvailable)
            elif wi == end:
                order.append(wi)
            toRemove = []
            for na in nextAvailable:
                if isConditionsFullfilled(na) and workerpool.assignWorker(sec + 1, na):
                    toRemove.append(na)
            for r in toRemove:
                nextAvailable.remove(r)

        sec += 1

    print(sec)
