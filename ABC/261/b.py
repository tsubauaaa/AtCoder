N = int(input())
table = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if table[i][j] == "W":
            if table[j][i] != "L":
                print("incorrect")
                exit()
        elif table[i][j] == "L":
            if table[j][i] != "W":
                print("incorrect")
                exit()
        elif table[i][j] == "D":
            if table[j][i] != "D":
                print("incorrect")
                exit()
        else:
            continue


print("correct")
