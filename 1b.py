import itertools

with open('1.txt', 'r') as f:
    freq = 0
    dev = f.readlines()
    s1 = [0]

    found = False
    round = 0
    for num in itertools.cycle(dev):
        print("round: ", round)
        for a in dev:
            i = int(a)
            freq = freq + i
            if freq in s1:
                found = True
                break

            s1.append(freq)
        
        round = round + 1

    print("first double: ", freq)
