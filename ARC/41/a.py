x, y = map(int, input().split())
k = int(input())

if y > k:
    ans = x + k
else:
    ans = x - (k - y) + y
print(ans)
