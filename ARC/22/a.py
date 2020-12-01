S = input().lower()
ict = [""] * 3
for s in S:
    if s == "i":
        ict[0] = "i"
    elif s == "c" and ict[0] == "i":
        ict[1] = "c"
    elif s == "t" and ict[0] == "i" and ict[1] == "c":
        ict[2] = "t"
    else:
        continue
for word in ict:
    if word == "":
        print("NO")
        exit()
print("YES")
