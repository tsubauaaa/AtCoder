N = int(input())
t = [int(input()) for _ in range(N)]
ans = 101
for i in range(2 ** N):
    g1_sum = 0
    g2_sum = 0
    for j in range(N):
        if (i >> j) & 1:
            g1_sum += t[j]
        else:
            g2_sum += t[j]
    ans = min(max(g1_sum, g2_sum), ans)
print(ans)
