N = int(input())
s = input()
t = input()
if s == t:
    print(N)
    exit()
r_s = s[::-1]
cnt = 0
for i in range(N):
    if r_s[i] == t[i]:
        cnt += 1
print(N * 2 - cnt)
