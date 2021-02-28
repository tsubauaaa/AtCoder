N = int(input())
ans = []
for i in range(2, N + 2):
    if i ** 2 > N:
        break
    j = 2
    while i ** j < N + 1:
        ans.append(i ** j)
        j += 1
print(N - len(set(ans)))
