N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
ans = [0] * 3
for i in range(N):
    if P[i] <= A:
        ans[0] += 1
    elif A + 1 <= P[i] <= B:
        ans[1] += 1
    elif B + 1 <= P[i]:
        ans[2] += 1
    else:
        continue
print(min(ans))
