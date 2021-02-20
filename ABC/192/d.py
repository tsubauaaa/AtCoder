def base_n_to_10(X, n):
    out = 0
    for i in range(1, len(X) + 1):
        out += int(X[-i]) * (n ** (i - 1))
    return out


X = input()
X_list = list(X)
M = int(input())
X_list.sort(reverse=True)
d = int(X_list[0])
ans = []
for i in range(d + 1, 10 ** 18):
    base_n = base_n_to_10(X, i)
    print(base_n)
    if base_n > M:
        break
    else:
        ans.append(base_n)
print(len(set(ans)))
