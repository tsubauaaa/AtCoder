X, Y, Z = map(int, input().split())
X -= Z
ans = 0

while X >= (Y + Z) * ans:
    ans += 1
print(ans if X >= (Y + Z) * ans else ans - 1)
