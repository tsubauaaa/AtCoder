N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_a = a[0]
c = a[0] * b[0]
for i in range(N):
    max_a = max(max_a, a[i])
    c = max(c, max_a * b[i])
    print(c)
