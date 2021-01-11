X, Y = map(int, input().split())

if X % Y == 0:
    print(-1)
    exit()

i = 1
while i * X <= 10 ** 18:
    i == 1
    if i * X % Y != 0:
        print(i * X)
        exit()
print(-1)
