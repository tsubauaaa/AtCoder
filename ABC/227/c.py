N = int(input())
ans = 0
# for i in range(1, N+1):
#     for j in range(i, N+1):
#         tmp = 0
#         for k in range(j, N+1):
#             tmp += 1
#             if i*j*k > N:
#                 break
#             else:
#                 print(i,j,k, tmp)
#                 ans += 1
        
# print(ans)
for i in range(1, N+1):
    # print(i)
    if i > 5000:
        break
    for j in range(i, N+1):
        if (N // (i*j))-(j-1) <= 0:
            break
        # print((N // (i*j))-(j-1))
        ans += (N // (i*j))-(j-1)
        
print(ans)