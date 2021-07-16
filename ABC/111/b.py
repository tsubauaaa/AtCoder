N = int(input())

for i in range(N, 1000):
    d = list(str(i))
    if len(set(d)) == 1:
        print(i)
        exit()
