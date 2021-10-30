N,M=map(int,input().split())

area = []
for i in range(N):
    B = list(map(int,input().split()))
    area.append(B)

i_list_before = []
j_list_before = []
for n in range(N):
    i_list = []
    j_list = []
    # print("B,i,j,n,m" )
    for m in range(M):
        flag = False
        for j in range(1, 8):
            if (area[n][m]+7-(j)) % 7 == 0:
                # print(area[n][m], (area[n][m]+7-(j)) // 7,j,n+1,m+1 )
                i_list.append((area[n][m]+7-(j)) // 7)
                j_list.append(j)
                flag = True
        
    if area[n][M-1] - area[n][0] != M-1:
        print("No")
        exit()

    if len(i_list_before) == 0 and len(j_list_before) == 0:
        i_list_before = i_list
        j_list_before = j_list
        continue

    if j_list_before != j_list:
        print("No")
        exit()
    
    if len(set(i_list)) != 1:
        print("No")
        exit()

    if i_list_before[0]+1 != i_list[0]:
        print("No")
        exit()

        
    if sum(i_list) - sum(i_list_before) != M:
        print("No")
        exit()

    i_list_before = i_list
    j_list_before = j_list
    
print("Yes")
