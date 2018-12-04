class Sheet:
    def __init__(self, sheetId, x, y, width, height):
        self.sheetId = sheetId 
        self.coveredCoordinates = set()

        for i in range(x, x+width):
            for j in range(y, y+height):
                self.coveredCoordinates.add((i,j))

def convertSheetString(s:str):
    sheetInfo = s.split(" ")
    sheetId = sheetInfo[0]
    coordiantes = sheetInfo[2].rstrip(":").split(",")
    size = sheetInfo[3].split("x")
    x = int(coordiantes[0])
    y = int(coordiantes[1])
    width = int(size[0])
    height = int(size[1])

    return Sheet(sheetId, x, y, width, height)

with open("3.txt", "r") as f:
    sheets = list(map(convertSheetString, f.readlines()))
    nbrOfSheets = len(sheets)

    for i, s in enumerate(sheets):
        otherIndex = 0
        isUniqueToAllother = True
        while isUniqueToAllother and otherIndex < nbrOfSheets:
            if i != otherIndex:
                if len(s.coveredCoordinates & sheets[otherIndex].coveredCoordinates) == 0:
                    otherIndex = otherIndex + 1
                else:
                    isUniqueToAllother = False
            else:
                otherIndex = otherIndex + 1
        if otherIndex == nbrOfSheets:
            print(s.sheetId)