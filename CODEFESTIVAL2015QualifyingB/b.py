from collections import Counter

N, M = map(int, input().split())
scores = list(map(int, input().split()))
c = Counter(scores)
ans = []
for k, v in c.items():
    if v > N / 2:
        ans.append(k)
print(*ans if len(ans) == 1 else "?")
