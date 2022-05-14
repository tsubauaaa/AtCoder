N = int(input())

memo = {}
for i in range(N):
    S, T = input().split()
    if S in memo:
        continue
    memo[S] = [i + 1, int(T)]

memo_sorted = sorted(memo.items(), key=lambda x: x[1][1], reverse=True)
print(memo_sorted[0][1][0])
