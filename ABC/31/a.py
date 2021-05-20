A, D = map(int, input().split())

up_a = (A + 1) * D
up_d = A * (D + 1)
ans = up_a
if up_a != up_d:
    ans = max(up_a, up_d)
print(ans)
