N = int(input())
H = list(map(int, input().split()))
i = 0
while True:
    if H[i + 1] != 0:
        H[i] -= 1
        i += 1
    else:
        