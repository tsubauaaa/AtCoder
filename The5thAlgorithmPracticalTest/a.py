S = input()

o = 0
x = 0

for s in S:
    if s == "o":
        o += 1
        if o == 3:
            print("o")
            exit()
        x = 0
    elif s == "x":
        x += 1
        if x == 3:
            print("x")
            exit()
        o = 0
print("draw")
