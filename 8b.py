with open("8.txt", "r") as f:
    entries = list(map(int, f.readline().split(" ")))
    metadataSum = 0
    currentIndex = 0
    branchIndex = 0
    branches = dict()
    while len(entries) > 0:
        while entries[currentIndex] != 0:
            currentIndex += 2
        if int(currentIndex/2) == 1:
            branchIndex += 1
        ml = entries[currentIndex + 1]
        metadata = entries[currentIndex+2:currentIndex+ml+2]
        if branchIndex not in branches.keys():
            branches[branchIndex] = []
        branches[branchIndex].append(metadata)
        metadataSum += sum(metadata)
        entries = entries[:currentIndex] + entries[currentIndex+2+ml:]
        if currentIndex != 0:
            entries[currentIndex - 2] = entries[currentIndex - 2] - 1
        currentIndex = 0
    
    for k in branches.keys():
        print(k, branches[k])
        print()