N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = [T[0]]
for i in range(N - 1):
    n = min(T[i + 1], ans[i] + S[i])
    ans.append(n)

if N > 1:
    if T[0] > ans[-1] + S[-1]:
        ans = [ans[-2] + S[-1]]
        for i in range(N - 1):
            n = min(T[i + 1], ans[i] + S[i])
            ans.append(n)


for ansi in ans:
    print(ansi)
