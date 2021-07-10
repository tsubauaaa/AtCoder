N = int(input())
C = sorted(map(int, input().split()))
ans = 1
for i in range(N):
    ans *= max(0, C[i] - i) % 1000000007
print(ans)
