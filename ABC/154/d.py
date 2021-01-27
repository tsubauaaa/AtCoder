N, K = map(int, input().split())
p = list(map(int, input().split()))
cs_p = [(p[0] + 1) / 2]
for pi in p[1:]:
    cs_p.append(cs_p[-1] + (pi + 1) / 2)
if N == K:
    print(cs_p[-1])
    exit()

ans = 0
for i in range(N - K):
    ans = max(ans, cs_p[i + K] - cs_p[i])
print(ans)
