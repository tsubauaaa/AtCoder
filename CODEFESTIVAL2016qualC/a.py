s = input()
exist_C = False
for si in s:
    if si == "C":
        exist_C = True
    if exist_C and si == "F":
        print("Yes")
        exit()
print("No")
