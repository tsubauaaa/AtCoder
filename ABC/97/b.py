X = int(input())
ans = 1
for i in range(1, X + 1):
    for j in range(2, X + 1):
        if i ** j <= X:
            ans = max(ans, i ** j)
        else:
            break
print(ans
