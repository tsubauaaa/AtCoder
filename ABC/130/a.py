N, X = map(int, input().split())
L = list(map(int, input().split()))
D = 0
ans = [0]
for i in range(1, N + 1):
    D += L[i - 1]
    ans.append(D)

cnt = 0
for i in range(len(ans)):
    cnt += 1
    if ans[i] > X:
        cnt -= 1
        break
print(cnt)
