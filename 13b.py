import itertools

with open("13test.txt", "r") as f:
    data = f.readlines()

    directions = {
        "<": ["v", "^"],
        ">": ["^", "v"],
        "v": [">", "<"],
        "^": ["<", ">"]
    }

    carts = []
    for y, row in enumerate(data):
        cartsOnRow = [(c, x, y, 0)
                      for x, c in enumerate(row) if c in directions.keys()]
        carts.extend(cartsOnRow)
        data[y] = data[y].replace("<", "-")
        data[y] = data[y].replace(">", "-")
        data[y] = data[y].replace("v", "|")
        data[y] = data[y].replace("^", "|")

    def intersection(c):
        d = c[3] % 3
        turned = ()
        if d == 0:
            turned = (directions[c[0]][0], c[1], c[2], c[3]+1)
        if d == 1:
            turned = (c[0], c[1], c[2], c[3]+1)
        if d == 2:
            turned = (directions[c[0]][1], c[1], c[2], c[3]+1)

        return turned

    while len(carts) != 0:
        carts.sort(key=lambda c: (c[2], c[1]))
        
        cartsToRemove=[]
        
        for c in carts

        for i, c in enumerate(carts):
            n = ""
            if c[0] == "<":
                n = data[c[2]][c[1]-1]
                if n == "-":
                    carts[i] = ("<", c[1]-1, c[2], c[3])
                if n == "/":
                    carts[i] = ("v", c[1]-1, c[2], c[3])
                if n == "\\":
                    carts[i] = ("^", c[1]-1, c[2], c[3])
                if n == "+":
                    t = intersection(c)
                    carts[i] = (t[0], t[1]-1, t[2], t[3])

            if c[0] == ">":
                n = data[c[2]][c[1]+1]
                if n == "-":
                    carts[i] = (">", c[1]+1, c[2], c[3])
                if n == "\\":
                    carts[i] = ("v", c[1]+1, c[2], c[3])
                if n == "/":
                    carts[i] = ("^", c[1]+1, c[2], c[3])
                if n == "+":
                    t = intersection(c)
                    carts[i] = (t[0], t[1]+1, t[2], t[3])

            if c[0] == "v":
                n = data[c[2]+1][c[1]]
                if n == "|":
                    carts[i] = ("v", c[1], c[2]+1, c[3])
                if n == "\\":
                    carts[i] = (">", c[1], c[2]+1, c[3])
                if n == "/":
                    carts[i] = ("<", c[1], c[2]+1, c[3])
                if n == "+":
                    t = intersection(c)
                    carts[i] = (t[0], t[1], t[2]+1, t[3])

            if c[0] == "^":
                n = data[c[2]-1][c[1]]
                if n == "|":
                    carts[i] = ("^", c[1], c[2]-1, c[3])
                if n == "\\":
                    carts[i] = ("<", c[1], c[2]-1, c[3])
                if n == "/":
                    carts[i] = (">", c[1], c[2]-1, c[3])
                if n == "+":
                    t = intersection(c)
                    carts[i] = (t[0], t[1], t[2]-1, t[3])

        print(carts)
        print()
