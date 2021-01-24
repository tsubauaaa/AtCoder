from collections import Counter

S = input()
C = Counter(S)
ans = [0] * 6
for k, v in C.items():
    if k == "A":
        ans[0] = v
    elif k == "B":
        ans[1] = v
    elif k == "C":
        ans[2] = v
    elif k == "D":
        ans[3] = v
    elif k == "E":
        ans[4] = v
    elif k == "F":
        ans[5] = v
print(*ans)
