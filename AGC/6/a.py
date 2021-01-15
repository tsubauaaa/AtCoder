N = int(input())
s = input()
t = input()
m = N
for i in range(N):
    if s[i:] == t[: N - i]:
        m = i
        break
print(N * 2 - (N - m))
