S = input()
w_cnt = 0
ans = 0
for i in range(len(S)):
    if S[i] == "W":
        ans += i - w_cnt
        w_cnt += 1
print(ans)
