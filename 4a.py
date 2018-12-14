from datetime import datetime, timedelta
import itertools

with open("4.txt", "r") as f:
    rawNotes = f.readlines()
    rawNotes.sort()

    sleepRecord = dict()
    currentGuard = -1
    fellAsleep = 0
    for note in rawNotes:
        n = note.split(" ")
        minute = int(n[1].split(":")[1].rstrip("]"))
        if n[2] == "Guard":
            currentGuard = int(n[3].lstrip("#"))
            if currentGuard not in sleepRecord:
                sleepRecord[currentGuard] = []
            sleepRecord[currentGuard].insert(0, set())
        if n[2] == "falls":
            fellAsleep = minute
        if n[2] == "wakes":
            sleepRecord[currentGuard][0].update(range(fellAsleep, minute))

    sumSleepRecords = {k: sum(map(lambda v: len(v), v))
                       for k, v in sleepRecord.items()}
    mostSleepy = max(sumSleepRecords.items(), key=lambda k: k[1])

    aggregate = []
    [aggregate.extend(shift) for shift in sleepRecord[mostSleepy[0]]]

    aggregate.sort()
    groups = {k: len(list(g)) for k, g in itertools.groupby(aggregate)}

    mostFrequentMinute = max(groups.items(), key=lambda k: k[1])[0]

    print(mostFrequentMinute * mostSleepy[0])
