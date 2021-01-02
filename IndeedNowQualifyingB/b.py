s = input()
t = input()
len_s = len(s)
cnt = 0
for i in range(len_s):
    if s == t:
        print(cnt)
        exit()
    s = s[-1] + s[0:-1]
    cnt += 1
print(-1)
