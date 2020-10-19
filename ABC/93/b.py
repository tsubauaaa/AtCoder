A, B, K = map(int, input().split())
all_nums = set()
for i in range(K):
    all_nums.add(A + i)
    all_nums.add(B - i)
ans = []
for num in all_nums:
    if A <= num <= B:
        ans.append(num)

ans.sort()

for a in ans:
    print(a)
