def g1(x):
    s_x = sorted(x, reverse=True)
    return int("".join(s_x))


def g2(x):
    s_x = sorted(x)
    return int("".join(s_x))


def f(x):
    return g1(x) - g2(x)


N, K = input().split()
N = list(N)
K = int(K)
ans = [-1] * K
for i in range(K):
    ans[i] = f(N)
    N = list(str(ans[i]))
print(ans[-1] if K != 0 else int("".join(N)))
