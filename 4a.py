import datetime

with open("4.txt", "r") as f:
    notes = f.readlines()
    notes.sort()
    guards = dict()
    nbrOfNotes = len(notes)
    currentIndex = 0
    while currentIndex < nbrOfNotes:
        noteParts = notes[currentIndex].split(" ")
        date = list(map(int, noteParts[0].lstrip("[").split("-")))
        time = list(map(int, noteParts[1].rstrip("]").split(":")))
        d = datetime.datetime(date[0], date[1], date[2], time[0], time[1])
        action = noteParts[2]
        guardId = str()
        if action == "Guard":
            guardId = noteParts[3]

