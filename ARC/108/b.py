N = int(input())
s = input()
t = "a" * N
for i in range(N):
    t[N - i] = s[i]

print(t)
