from collections import Counter

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

BC = [B[C[i]-1] for i in range(N)]
c = Counter(BC)

ans = 0
for i in range(N):
    ans += c[A[i]]

print(ans)