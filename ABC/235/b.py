N = int(input())
H = list(map(int, input().split()))

now = H[0]

for i in range(1, N):
    if H[i] > now:
        now = H[i]
    else:
        break
print(now)
