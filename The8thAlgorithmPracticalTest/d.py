X, Y = map(int, input().split())


def count_div(n):
    div = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            div.append(i)
            div.append(n // i)
        i += 1
    return len(set(div))


cnt_X = count_div(X)
cnt_Y = count_div(Y)

if cnt_X > cnt_Y:
    print("X")
elif cnt_X < cnt_Y:
    print("Y")
else:
    print("Z")
