N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(2, max(A) + 1):
    tmp = 0
    for j in range(N):
        if A[j] % i == 0:
            tmp += 1
    ans.append(tmp)
print(ans.index(max(ans)) + 2)
