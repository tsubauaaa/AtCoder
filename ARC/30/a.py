n = int(input())
k = int(input())
vertex = 0

ans = "NO"
for i in range(0, n, 2):
    vertex += 1
    if n % 2 == 0:
        alpha = 0
    else:
        alpha = -1
    cnt = vertex + alpha
    if cnt == k:
        # print(vertex)
        ans = "YES"
        break
print(ans)
