N = int(input())


def count_div(n):
    div = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            div.append(i)
            div.append(n // i)
        i += 1
    return len(div)


ans = 0
for i in range(1, N + 1):
    if i % 2 != 0:
        if count_div(i) == 8:
            ans += 1
    else:
        continue
print(ans)
