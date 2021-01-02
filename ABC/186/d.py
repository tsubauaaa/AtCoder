N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
cs_A = [A[0]]
for a in A[1:]:
    cs_A.append(cs_A[-1] + a)
ans = 0
for i in range(N - 1):
    ans += A[i] * (N - i - 1) - (cs_A[-1] - cs_A[i])
print(ans)
