N = int(input())
flowers = {}
for i in range(N):
    A = int(input())
    if A in flowers:
        flowers[A] += 1
    else:
        flowers[A] = 1
ans = 0
for k, v in flowers.items():
    ans += v - 1
print(ans)

