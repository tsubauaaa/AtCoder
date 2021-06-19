import collections

N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
c = dict(c)


ans = 0
for i in range(N):
    c[A[i]] -= 1
    ans += (N - i - 1) - c[A[i]]
print(ans)
