N, M = map(int, input().split())

f = {}

for i in range(N):
    KA = list(map(int, input().split()))
    f[i + 1] = set(KA[1:])

P, Q = map(int, input().split())
B = set(map(int, input().split()))
ans = 0
for k, v in f.items():
    if len(v & B) >= Q:
        ans += 1

print(ans)
