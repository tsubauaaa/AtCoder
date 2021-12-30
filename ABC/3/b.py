S = input()
T = input()

at = ["a", "t", "c", "o", "d", "e", "r"]

for s, t in zip(S, T):
    if s != "@" and t != "@":
        if s != t:
            print("You will lose")
            exit()
        else:
            continue
    elif s == "@" and t != "@":
        if t not in at:
            print("You will lose")
            exit()
        else:
            continue
    elif s != "@" and t == "@":
        if s not in at:
            print("You will lose")
            exit()
        else:
            continue
    else:
        continue
print("You can win")
