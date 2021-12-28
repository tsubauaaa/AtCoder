N, W = map(int, input().split())
deliciousness = []
for i in range(N):
    AB = list(map(int, input().split()))
    deliciousness.append(AB)

sorted_deli = sorted(deliciousness, reverse=True)
w = 0
ans = 0
index = 0
done = True
for i, d in enumerate(sorted_deli):
    w += d[1]
    if w > W:
        w -= d[1]
        index = i
        done = False
        break
    ans += d[0] * d[1]

alpha = 0 if done else (W - w) * sorted_deli[index][0]
print(ans + alpha)
