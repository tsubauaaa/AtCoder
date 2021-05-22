S=input()
ans = ""
for s in S[::-1]:
    if s == "6":
        ans += "9"
    elif s == "9":
        ans += "6"
    else:
        ans += s
print(ans)