with open('1.txt', 'r') as f:
    print(sum(map(int, f.readlines())))