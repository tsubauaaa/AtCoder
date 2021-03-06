N = int(input())
A = list(map(int, input().split()))
cs_A = [A[0]]
cs_A2 = [A[0] ** 2]
for x in A[1:]:
    cs_A.append(cs_A[-1] + x)
    cs_A2.append(cs_A2[-1] + x ** 2)
sum_A = []
ans = 0
for i in range(N - 1):
    alpha = cs_A[-1] - cs_A[i - 1] if i != 0 else cs_A[-1]
    ans += A[i] ** 2 * (N - i + 1) + (cs_A2[-1] - cs_A2[i]) - 2 * A[i] * alpha
print(ans)
