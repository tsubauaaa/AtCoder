H, W = map(int, input().split())
S = []
H_ans = 0
W_ans = 0
for i in range(H):
    S.append(input())

for h in range(H):
    for w in range(W - 1):
        if S[h][w] == "." and S[h][w + 1] == ".":
            W_ans += 1

for h in range(H - 1):
    for w in range(W):
        if S[h][w] == "." and S[h + 1][w] == ".":
            H_ans += 1


print(W_ans + H_ans)
