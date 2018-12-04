with open("2.txt", "r") as f:
    ids = f.readlines()

    cleaned = []

    for i in ids:
        chars = list(i)
        chars.remove('\n')
        cleaned.append(chars)
    
    for i, c in enumerate(cleaned):
        for j in cleaned[i+1:]:
            jCopy = j.copy()
            for char in c:
                if jCopy.__contains__(char):
                    jCopy.remove(char)
            if len(jCopy) == 1:
                strIndx = 0
                diffCount = 0
                while strIndx < len(c):
                    if c[strIndx] != j[strIndx]:
                        diffCount = diffCount + 1
                    strIndx = strIndx + 1
                if diffCount == 1:
                    print(''.join(c))
                    print(''.join(j))

