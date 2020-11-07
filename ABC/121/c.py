N, M = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(N)]
store = sorted(store)
bought = M
ans = 0
for i in range(N):
    if bought == 0:
        break
    if store[i][1] < bought:
        ans += store[i][0] * store[i][1]
        bought -= store[i][1]
    else:
        ans += store[i][0] * bought
        bought -= bought

print(ans)
