from itertools import combinations


def triangle(leng):
    return (
        leng[0] + leng[1] > leng[2]
        and leng[1] + leng[2] > leng[0]
        and leng[2] + leng[0] > leng[1]
    )


N = int(input())
L = list(map(int, input().split()))
ans = 0
for c in combinations(L, 3):
    if c[0] == c[1] or c[0] == c[2] or c[1] == c[2]:
        continue
    if triangle(c):
        ans += 1

print(ans)
