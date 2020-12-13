N = int(input())
usable = [True] * (2 * 10 ** 5 + 1)
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    usable[num] = False
    for i in range(ans, len(usable)):
        if usable[i]:
            ans = i
            print(ans)
            break
