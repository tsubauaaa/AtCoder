N, K = map(int, input().split())
H = list(map(int, input().split()))
if K == 0:
    print(sum(H))
    exit()
if N <= K:
    print(0)
    exit()
H.sort(reverse=True)
ans = 0
for i in range(K, len(H)):
    ans += H[i]
print(ans)
