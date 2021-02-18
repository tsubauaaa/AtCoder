S = input()
T = input()
for s, t in zip(S, T[:-1]):
    if s != t:
        print("No")
        exit()
print("Yes")
