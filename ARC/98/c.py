N = int(input())
S = input()

min_turn = 300000

sum_W = [0]

for i in range(N):
    if S[i] == "W":
        sum_W.append(sum_W[i]+1)
    else:
        sum_W.append(sum_W[i]+0)


for i in range(N):
    w = sum_W[i]
    e = (N-1-i) - (sum_W[N] - sum_W[i+1])

    turn = w+e

    min_turn = min(turn, min_turn)

print(min_turn)
