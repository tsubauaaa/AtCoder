N = int(input())
z = []
for i in range(1, 600000):
    j = set(list(str(i)))
    if len(j) == 1:
        z.append(i)
print(z[N - 1])
