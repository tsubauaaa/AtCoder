N = int(input())

trees = {i: 0 for i in range(N)}

for i in range(N-1):
    a,b=map(int,input().split())
    trees[a-1] += 1
    trees[b-1] += 1

for k, v in trees.items():
    if v == N -1:
        print("Yes")
        exit()
print("No")