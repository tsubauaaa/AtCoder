a = int(input())
b = int(input())

for i in range(1, 100):
    if i * b >= a:
        print(i * b - a)
        exit()
