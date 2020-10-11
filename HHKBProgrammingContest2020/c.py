N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    print(set(P[0 : i + 1]))
