N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    # print(f"{A}, {i}")
    ans += min(B[i], A[i] + A[i + 1])
    if A[i] + A[i + 1] < B[i]:
        A[i + 1] = 0
        A[i] = 0
    elif A[i] < B[i]:
        A[i + 1] += A[i] - B[i]
        A[i] = 0
    else:
        A[i] -= B[i]

print(ans)
