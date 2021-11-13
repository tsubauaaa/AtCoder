N = int(input())
S = list(map(int, input().split()))
ans = 0
for s in S:
    for b in range(1, 100):
        if (s - 3*b) % (4 * b + 3) == 0:
            break
    else:
        ans += 1
            

print(ans)