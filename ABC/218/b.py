P=list(map(int, input().split()))

ans = ""

for p in P:
    ans += chr(96+p)

print(ans)