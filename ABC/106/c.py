S = input()
K = int(input())
ans = 0
cnt = 0
for i in range(K):
    if S[i] != "1":
        ans = int(S[i])
        break
    else:
        cnt += 1
    if cnt == K:
        ans = 1

print(ans)
