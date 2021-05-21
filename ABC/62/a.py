x, y = map(int, input().split())

groups = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]

ans = "No"
for g in groups:
    if x in g and y in g:
        ans = "Yes"
print(ans)