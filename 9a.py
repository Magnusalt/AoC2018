import itertools


class Node:
    def __init__(self, next, prev, value):
        if next == None and prev == None:
            self.next = self
            self.prev = self
        else:
            self.next = next
            self.prev = prev
        self.value = value


players = 464
lastMarbleScore = 71730 * 100

currentMarble = 2

scoreBoard = {p: 0 for p in range(players)}

first = Node(None, None, 0)

currentNode = Node(first, first, 1)
first.next = currentNode
first.prev = currentNode

for player in itertools.cycle(range(players)):
    if currentMarble % 23 == 0:
        special = currentNode.prev.prev.prev.prev.prev.prev.prev
        scoreBoard[player] += (special.value + currentMarble)
        currentNode = special.next

        special.prev.next = special.next
        special.next.prev = special.prev
    else:
        nextCurrent = Node(currentNode.next.next,
                           currentNode.next, currentMarble)
        currentNode.next.next.prev = nextCurrent
        currentNode.next.next = nextCurrent
        currentNode = nextCurrent
    if lastMarbleScore == currentMarble:
        break
    currentMarble += 1


print(max(scoreBoard.values()))
