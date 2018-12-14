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
    
    allGuardsMostFreq = dict()
    for k, v in sleepRecord.items():
        minutes = []
        for m in v:
            minutes.extend(m)
        minutes.sort()
        grouped = {k: len(list(g)) for k, g in itertools.groupby(minutes)}

        if len(grouped) > 0:
            allGuardsMostFreq[k] = max(grouped.items(), key=lambda m: m[1])
    
    mostFrequentMinute = max(allGuardsMostFreq.items(), key=lambda m: m[1][1])

    print(mostFrequentMinute[0] * mostFrequentMinute[1][0])
        