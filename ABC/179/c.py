N = int(input())

ans = 0

for a in range(1, N):
    b_count = (N-1) // a
    ans += b_count
print(ans)
