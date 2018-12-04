with open("3.txt", "r") as f:
    sheets = f.readlines()
    totalOverlap = 0
    coveredCoordinates = dict()
    for s in sheets:
        s = list(map(str.strip, s.split("@")[1].split(":")))
        pos = list(map(int, s[0].split(",")))
        size = list(map(int, s[1].split("x")))
        xEnd = pos[0] + size[0]
        yEnd = pos[1] + size[1]

        for x in range(pos[0], xEnd):
            for y in range(pos[1], yEnd):
                if (x, y) not in coveredCoordinates.keys():
                    coveredCoordinates[(x,y)] = 1
                else:
                    if coveredCoordinates[(x, y)] == 1:
                        totalOverlap = totalOverlap + 1
                        coveredCoordinates[(x, y)] = 2
    print(totalOverlap)