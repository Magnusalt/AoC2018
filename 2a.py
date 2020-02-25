import itertools

with open("2.txt", "r") as f:
    ids = f.readlines()
    
    twoTimes = 0
    threeTimes = 0

    for i in ids:
        chars = list(i)
        chars.remove('\n')
        chars.sort()
        group = []
        keys = []
        for k, g in itertools.groupby(chars):
            group.append(list(g))
            keys.append(k)
        lengths = list(map(len, group))
        if 2 in lengths:
            twoTimes = twoTimes + 1
        if 3 in lengths:
            threeTimes = threeTimes + 1
        
    print("two times ", twoTimes, "three times ", threeTimes, "prod ", twoTimes * threeTimes)

