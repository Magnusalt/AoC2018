from multiprocessing import Pool

dim = 300
serial_nbr = 9798


def calculatePowerLevel(x, y, serial_nbr):
    rackId = x + 10
    powerLevel = str((rackId * y + serial_nbr) * rackId)
    if len(powerLevel) > 2:
        p = powerLevel[::-1][2]
        return int(p) - 5
    else:
        return -5

grid = [[calculatePowerLevel(x, y, serial_nbr)
                 for y in range(1, dim+1)] for x in range(1, dim+1)]


def compute(square_size):
    print("processing size: ", square_size)
    maxPower = 0
    coordinatesWithMax = (1, 1)
    size = 0
    for x in range(dim-(square_size-1)):
        for y in range(dim-(square_size-1)):
            three_by_three_sum = 0
            for inner in range(square_size):
                three_by_three_sum += sum(grid[x+inner][y:y+square_size])
            if three_by_three_sum > maxPower:
                maxPower = three_by_three_sum
                coordinatesWithMax = (x+1, y+1)
                size = square_size
    return (maxPower, coordinatesWithMax, size)


def main():
    if __name__ == '__main__':
        sizes = [square_size for square_size in range(1, 301)]
        with Pool() as p:
            r = p.map(compute, sizes)
            print(max(r, key=lambda r: r[0]))


main()
