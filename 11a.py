def calculatePowerLevel(x, y, serial_nbr):
    rackId = x + 10
    powerLevel = str((rackId * y + serial_nbr) * rackId)
    if len(powerLevel) > 2:
        p = powerLevel[::-1][2]
        return int(p) - 5
    else:
        return -5


def main(dim, serial_nbr):
    grid = [[calculatePowerLevel(x, y, serial_nbr)
             for y in range(1, dim+1)] for x in range(1, dim+1)]
    maxPower = 0
    coordinatesWithMax = (1, 1)
    for x in range(dim-2):
        for y in range(dim-2):
            three_by_three_sum = 0
            for x_inner in range(3):
                for y_inner in range(3):
                    three_by_three_sum += grid[x+x_inner][y+y_inner]
            if three_by_three_sum > maxPower:
                maxPower = three_by_three_sum
                coordinatesWithMax = (x+1, y+1)

    print(maxPower, coordinatesWithMax)


main(300, 9798)
