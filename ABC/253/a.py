a, b, c = map(int, input().split())

ans = "No"

if a <= b <= c:
    ans = "Yes"

if c <= b <= a:
    ans = "Yes"

print(ans)
