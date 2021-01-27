ranks = [int(input()) for _ in range(3)]
s_ranks = sorted(ranks, reverse=True)
ans = [0] * 3
for i in range(3):
    ans[i] = s_ranks.index(ranks[i])
for ansi in ans:
    print(ansi + 1)
