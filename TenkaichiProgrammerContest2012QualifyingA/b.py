C = input().replace(",", "0")
C = C.replace(" ", ",")
C = [c for c in C]
for i in range(len(C) - 1):
    if C[i] == "," and C[i + 1] == ",":
        C[i] = "x"
ans = ""
for c in C:
    if c == "x":
        continue
    elif c == "0":
        ans += ans.join(",")
    else:
        ans += ans.join(c)
print(ans)
