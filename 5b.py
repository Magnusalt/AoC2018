import string

with open("5.txt", "r") as f:
    polymer = list(f.readline())

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    alphabetLength = len(lowercase)

    resultingLengths = []

    for c in range(0, alphabetLength):
        stack = []
        polymerHead, *polymerTail = polymer

        while polymerHead != "":

            if polymerHead == lowercase[c] or polymerHead == uppercase[c]:
                if len(polymerTail) != 0:
                    polymerHead, *polymerTail = polymerTail
                else:
                    polymerHead = ""
                continue
            if len(stack) == 0:
                stack.append(polymerHead)
            else:
                stackTop = stack.pop()
                if abs(ord(stackTop)-ord(polymerHead)) != 32:
                    stack.extend([stackTop, polymerHead])

            if len(polymerTail) != 0:
                polymerHead, *polymerTail = polymerTail
            else:
                polymerHead = ""

        print(uppercase[c], len(stack))
        resultingLengths.append(len(stack))
    
    print(min(resultingLengths))
