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
        if lengths.__contains__(2):
            twoTimes = twoTimes + 1
        if lengths.__contains__(3):
            threeTimes = threeTimes + 1
        
    print("two times ", twoTimes, "three times ", threeTimes, "prod ", twoTimes * threeTimes)

