with open("8.txt", "r") as f:
    entries = list(map(int, f.readline().split(" ")))
    metadataSum = 0
    currentIndex = 0
    while len(entries) > 0:
        while entries[currentIndex] != 0:
            currentIndex += 2
        ml = entries[currentIndex + 1]
        metadataSum += sum(entries[currentIndex+2:currentIndex+ml+2])
        entries = entries[:currentIndex] + entries[currentIndex+2+ml:]
        if currentIndex != 0:
            entries[currentIndex - 2] = entries[currentIndex - 2] - 1
        currentIndex = 0
    print(metadataSum)