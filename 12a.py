import time
import matplotlib.pyplot as plt

initalState = "##..##....#.#.####........##.#.#####.##..#.#..#.#...##.#####.###.##...#....##....#..###.#...#.#.#.#"
rules = [
    ("##.#.", "."),
    ("##.##", "."),
    ("#..##", "."),
    ("#.#.#", "."),
    ("..#..", "#"),
    ("#.##.", "."),
    ("##...", "#"),
    (".#..#", "."),
    ("#.###", "."),
    (".....", "."),
    ("...#.", "#"),
    ("#..#.", "#"),
    ("###..", "#"),
    (".#...", "#"),
    ("###.#", "#"),
    ("####.", "."),
    (".##.#", "#"),
    ("#.#..", "#"),
    (".###.", "#"),
    (".#.##", "."),
    ("#####", "#"),
    ("....#", "."),
    (".####", "."),
    (".##..", "#"),
    ("##..#", "."),
    ("#...#", "."),
    ("..###", "#"),
    ("...##", "."),
    ("#....", "."),
    ("..##.", "."),
    (".#.#.", "#"),
    ("..#.#", "#")
]

rulesDict = {kv[0]: kv[1] for kv in rules}


def getNextGen(sequence):
    return rulesDict[sequence]


class Pot:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.nextGenValue = ""
        self.next = None
        self.prev = None

    def getTwoLeft(self):
        if self.prev == None or self.prev.prev == None:
            return "."
        return self.prev.prev.value

    def getOneLeft(self):
        if self.prev == None:
            return "."
        return self.prev.value

    def getTwoRight(self):
        if self.next == None or self.next.next == None:
            return "."
        return self.next.next.value

    def getOneRight(self):
        if self.next == None:
            return "."
        return self.next.value

    def calculateNextGeneration(self):
        order = self.getTwoLeft() + self.getOneLeft() + self.value + \
            self.getOneRight() + self.getTwoRight()
        self.nextGenValue = getNextGen(order)

    def applyNextGeneration(self):
        self.value = self.nextGenValue


def main():
    zero = None
    current = None
    prev = None
    for i, p in enumerate(initalState):
        if i == 0:
            zero = Pot(p, i)
            minusOne = Pot(".", i-1)
            minusTwo = Pot(".", i-2)
            minusTwo.next = minusOne
            minusOne.prev = minusTwo
            current = zero
            minusOne.next = current
            current.prev = minusOne
        else:
            prev = current
            current = Pot(p, i)
            current.prev = prev
            prev.next = current
    plusOne = Pot(".", current.index + 1)
    plusTwo = Pot(".", current.index + 2)
    plusOne.prev = current
    plusOne.next = plusTwo
    plusTwo.prev = plusOne
    current.next = plusOne
    current = current.next.next

    #generations = 50000000000
    generations = 5000
    perf = []
    for g in range(generations):
        start = time.perf_counter()
        cleanUp = False
        if g%100 == 0 and g > 0:
            cleanUp = True
            print("will clean up")

        while current.prev != None:
            current.calculateNextGeneration()
            current = current.prev

        current.calculateNextGeneration()
        if current.value == "#" or current.next.value == "#" or current.next.next.value == "#":
            minusOne = Pot(".", current.index - 1)
            minusTwo = Pot(".", current.index - 2)
            minusTwo.next = minusOne
            minusOne.prev = minusTwo
            minusOne.next = current
            current.prev = minusOne
            current = current.prev
            current.calculateNextGeneration()
            current = current.prev
            current.calculateNextGeneration()

        if cleanUp:
            print("cleaning")
            while current.next.next.next.next.next == "." \
            and current.next.next.next.next == "."\
            and current.next.next.next == "."\
            and current.next.next == "."\
            and current.next == "."\
            and current == ".":
                current = current.next
            current.prev = None
            cleanUp = False

        while current.next != None:
            current.applyNextGeneration()
            current = current.next

        if current.value == "#" or current.prev.value == "#" or current.prev.prev.value == "#":
            plusOne = Pot(".", current.index + 1)
            plusTwo = Pot(".", current.index + 2)
            plusOne.prev = current
            plusOne.next = plusTwo
            plusTwo.prev = plusOne
            current.next = plusOne
            current = current.next.next
        
        stop = time.perf_counter()
        perf.append((g, stop-start))

    plt.plot(list(map(lambda p: p[0], perf)), list(map(lambda p: p[1], perf)))
    plt.show()

    indexSum = 0
    while current.prev != None:
        current = current.prev
        if current.value == "#":
            indexSum += current.index

    print(indexSum)


main()
