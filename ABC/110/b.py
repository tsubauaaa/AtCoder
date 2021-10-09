N,M,X,Y=map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

max_x = max(x)
min_y = min(y)

for Z in range(-100, 101):
    if X < Z <= Y and max_x < Z and min_y >= Z:
        print("No War")
        exit()
print("War") 
