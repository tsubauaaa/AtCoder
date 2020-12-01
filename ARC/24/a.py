L, R = map(int, input().split())
ll = list(map(int, input().split()))
rr = list(map(int, input().split()))
ans = 0
for i in range(len(ll)):
    for j in range(len(rr)):
        if ll[i] == rr[j]:
            ans += 1
            del rr[j]
            break
print(ans)
