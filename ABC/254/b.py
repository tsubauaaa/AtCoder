N = int(input())

a = []

for i in range(N):
    aij = []
    for j in range(i + 1):
        if j == 0 or i == j:
            aij.append(1)
        else:
            aij.append(a[i - 1][j - 1] + a[i - 1][j])
    a.append(aij)
    print(*aij)
