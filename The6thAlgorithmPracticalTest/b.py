S = input()
i = 0
j = 0
while i <= len(S) - 4:
    j += 1
    if S[i : i + 4] == "post":
        print(j)
        exit()
    i += 4

print("none")
