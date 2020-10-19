N = int(input())
W = [input() for i in range(N)]
ans = "Yes"
if len(set(W)) != N:
    ans = "No"
else:
    last_word = W[0][0]
    for w in W:
        if last_word != w[0]:
            ans = "No"
        last_word = w[-1]
print(ans)
