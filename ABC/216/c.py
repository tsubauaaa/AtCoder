N=int(input())
n = 120


for k in range(1, n+1):
    for i in range(2**k):
        ans = ""
        cnt = 0
        for j in range(k):
            if (i>>j) & 1:
                cnt +=1
                ans += "A"
            else:
                cnt *= 2
                ans += "B"
            if cnt > N:
                break
        if cnt == N:
            print(ans)
            exit()
        

# print(ans)
# cnt = 0
# for ansi in ans:
#     if ansi == "A":
#         cnt += 1
#     else:
#         cnt *=2

# print(cnt)