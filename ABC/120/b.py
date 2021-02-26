A, B, K = map(int, input().split())
max_n = max(A, B)
ans = []
for i in range(1, max_n + 1):
    if A % i == 0 and B % i == 0:
        ans.append(i)
ans.sort(reverse=True)
print(ans[K - 1])
