
def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("6.txt", "r") as f:
    coordinates = []
    for line in f.readlines():
        current = line.rstrip("\n").split(",")
        coordinates.append((int(current[0]), int(current[1])))

    areaOwned = {c: [0, False] for c in coordinates}

    minX = min(coordinates, key=lambda c: c[0])[0]
    maxX = max(coordinates, key=lambda c: c[0])[0]
    minY = min(coordinates, key=lambda c: c[1])[1]
    maxY = max(coordinates, key=lambda c: c[1])[1]
    xRange = range(minX, maxX + 1)
    yRange = range(minY, maxY + 1)
    
    def isInfinite(p):
        print(p)
        return p[0] == minX or p[0] == maxX or p[1] == minY or p[1] == maxY

    matrix = [[[((x, y), c, manhattanDistance((x,y),c)) for c in coordinates] for x in xRange] for y in yRange]

    for y in range(len(xRange)):
        for x in range(len(yRange)):
            matrix[x][y].sort(key=lambda p: p[2])
            if not areaOwned[matrix[x][y][0][1]][1]:
                areaOwned[matrix[x][y][0][1]][1] = isInfinite(matrix[x][y][0][0])
            if matrix[x][y][0][2] != matrix[x][y][1][2]:
                areaOwned[matrix[x][y][0][1]][0] += 1

    print(areaOwned)

    print(max(filter(lambda v: not v[1], areaOwned.values())))