
def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("6.txt", "r") as f:
    coordinates = []
    for line in f.readlines():
        current = line.rstrip("\n").split(",")
        coordinates.append((int(current[0]), int(current[1])))

    minX = min(coordinates, key=lambda c: c[0])[0]
    maxX = max(coordinates, key=lambda c: c[0])[0]
    minY = min(coordinates, key=lambda c: c[1])[1]
    maxY = max(coordinates, key=lambda c: c[1])[1]
    xRange = range(minX, maxX + 1)
    yRange = range(minY, maxY + 1)
    
    matrix = [[[((x, y), c, manhattanDistance((x,y),c)) for c in coordinates] for x in xRange] for y in yRange]

    areaLessThan10000 = 0
    for y in range(len(xRange)):
        for x in range(len(yRange)):
            if sum(map(lambda a: a[2], matrix[x][y])) < 10000:
                areaLessThan10000 +=1
    
    print(areaLessThan10000)