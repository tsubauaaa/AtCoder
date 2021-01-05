from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
cntr = Counter(A)
sum_A = sum(A)
ans = [0] * Q
for i in range(Q):
    B, C = map(int, input().split())
    sum_A += -1 * B * cntr[B] + C * cntr[B]
    ans[i] = sum_A
    cntr[C] += cntr[B] * 1
    cntr[B] = 0
for ansi in ans:
    print(ansi)
