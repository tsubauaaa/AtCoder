N, K = map(int, input().split())
sunukes = [0] * N
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in range(d):
        sunukes[A[j] - 1] += 1

print(sunukes.count(0))
