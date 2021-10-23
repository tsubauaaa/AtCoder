import itertools
 
N = int(input())
 
points = []
 
for i in range(N):
    points.append(list(map(int, input().split())))
 
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            area = abs((points[i][0]-points[k][0]) * (points[j][1]-points[k][1]) - (points[j][0]-points[k][0]) * (points[i][1]-points[k][1]))
            if area > 0:
                ans += 1
print(ans)