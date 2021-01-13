N = int(input())
M = 0
for i in range(2, N + 1):
    if N % i == 0:
        M = i
        break
if N == M:
    print("YES")
    exit()
print("NO")
