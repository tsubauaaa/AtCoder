S = input()
odds = ["R", "U", "D"]
evens = ["L", "U", "D"]

for i in range(len(S)):
    if (i + 1) % 2 == 0:
        if S[i] not in evens:
            print("No")
            exit()
    else:
        if S[i] not in odds:
            print("No")
            exit()
print("Yes")
