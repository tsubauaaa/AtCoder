N = int(input())

score = {}

for i in range(N):
    S = input()
    if S in score:
        score[S] += 1
    else:
        score[S] = 1

    if score[S] == 1:
        print(S)
    else:
        print(S + f"({score[S]-1})")
