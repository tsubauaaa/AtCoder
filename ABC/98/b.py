N = int(input())
S = input()
ans = 0
for i in range(1, N):
    tmp = 0
    X = "".join(sorted(set(S[:i])))
    Y = "".join(sorted(set(S[i:])))
    for x in X:
        for y in Y:
            if x == y:
                tmp += 1
    ans = max(ans, tmp)
print(ans)
