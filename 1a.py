with open('1.txt', 'r') as f:
    freq = 0
    dev = f.readlines()
    
    for a in dev:
        i = int(a)
        freq = freq + i
    
    print(freq)