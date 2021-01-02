n = int(input())

if (
    1 <= n <= 20
    or 41 <= n <= 60
    or 81 <= n <= 100
    or 121 <= n <= 140
    or 161 <= n <= 180
):
    print(n % 20 if n % 20 != 0 else 20)
else:
    print(20 - n % 20 + 1 if n % 20 != 0 else 1)
