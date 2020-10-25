S = input()
n = S.count("N")
s = S.count("S")
e = S.count("E")
w = S.count("W")
ans = "Yes"
if n > 0 and s == 0:
    ans = "No"
elif s > 0 and n == 0:
    ans = "No"
elif e > 0 and w == 0:
    ans = "No"
elif w > 0 and e == 0:
    ans = "No"
print(ans)
