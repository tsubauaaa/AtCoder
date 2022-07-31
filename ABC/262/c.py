N = int(input())
a = list(map(int, input().split()))

memo = {}
for i in range(N):
    memo[i + 1] = a[i]

sorted_memo = sorted(memo.items(), key=lambda i: i[1])

# print(dict(sorted_memo))
ans = 0
for k, v in dict(sorted_memo).items():
    if memo[v] == k:
        if k == v:
            continue
        ans += 1
ans1 = 0
for k, v in dict(sorted_memo).items():
    if k == v:
        ans1 += 1

print(ans // 2 + (ans1 - 1) * ans1 // 2)
