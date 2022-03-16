S = input()
a = 0
b = 0
c = 0
ans = "a"
for s in S:
    if s == "a":
        a += 1
    elif s == "b":
        b += 1
    else:
        c += 1

    if a > b and a > c:
        ans = "a"
    elif b > a and b > c:
        ans = "b"
    else:
        ans = "c"

print(ans)
