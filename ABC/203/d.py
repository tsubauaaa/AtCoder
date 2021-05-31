N,K=map(int,input().split())
districts = [list(map(int, input().split())) for i in range(N)]

print("--------")
for i in range(K):
    for j in range(K):
        print(i+1,j+1)
print("--------")
for i in range(K):
    for j in range(K):
        j += 1
        if j+1 > K:
            break
        print(i+1,j+1)
print("--------")
for i in range(K):
    i += 1
    if i+1 > K:
        break
    for j in range(K):
        
        print(i+1,j+1)
print("--------")
for i in range(K):
    i += 1
    if i+1 > K:
        break
    for j in range(K):
        j += 1        
        if j+1 > K:
            break
        print(i+1,j+1)
