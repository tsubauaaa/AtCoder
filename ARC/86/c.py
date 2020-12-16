from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
c = Counter(A).most_common()[::-1]
d = len(c) - K
if d <= 0:
    print(0)
    exit()
ans = 0
for i in range(d):
    ans += c[i][1]
print(ans)
