N = int(input())
A = sorted(map(int, input().split()))

ans = "Yes"
for i in range(1, N + 1):
    if A[i - 1] != i:
        ans = "No"
print(ans)
