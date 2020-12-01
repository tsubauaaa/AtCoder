N, K = map(int, input().split())
t = [int(input()) for _ in range(N)]
for i in range(N - 2):
    if t[i] + t[i + 1] + t[i + 2] < K:
        print(i + 1 + 2)
        break
else:
    print(-1)
