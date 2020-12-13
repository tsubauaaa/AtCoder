S = input()
ans = ""
for s in S:
    if s in ("O", "D"):
        ans += ans.join("0")
    elif s == "I":
        ans += ans.join("1")
    elif s == "Z":
        ans += ans.join("2")
    elif s == "S":
        ans += ans.join("5")
    elif s == "B":
        ans += ans.join("8")
    else:
        ans += ans.join(s)
print(ans)
