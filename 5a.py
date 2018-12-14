with open("5.txt", "r") as f:
    polymer = list(f.readline())
    stack = []

    polymerHead, *polymerTail = polymer

    while polymerHead != "":

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
        

    print(len(stack))