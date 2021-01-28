S = input()
ans = ""
for s in S:
    if s.isdecimal():
        ans += ans.join(s)
print(ans)
