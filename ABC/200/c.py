N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if (A[i] - A[j]) % 200 == 0:
            print(A[i], A[j], A[i] % 200, A[j] % 200)
            ans += 1
print(ans)
