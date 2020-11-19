def is_ok(n):
    return A * n + B * len(str(n)) <= X


A, B, X = map(int, input().split())

left = 0
right = 10 ** 9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if is_ok(mid):
        left = mid
    else:
        right = mid
print(left)
