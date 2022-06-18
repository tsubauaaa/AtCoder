N = int(input())
A = list(map(int, input().split()))

masu = []
P = 0
for i in range(N):
    masu.append(0)
    for j in range(i + 1):
        if masu[j] + A[i] >= 4:

            P += 1
            masu[j] = -1000
            continue
        masu[j] += A[i]

print(P)
