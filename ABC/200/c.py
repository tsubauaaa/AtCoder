from collections import Counter

N = int(input())
A = list(map(int, input().split()))
R = [a % 200 for a in A]

ans = 0
for k, v in Counter(R).items():
    if v > 1:
        ans += v * (v - 1) // 2
print(ans)
