N = int(input())
div = []
i = 1
while i * i <= N:
    if N % i == 0:
        div.append(i)
        div.append(N // i)
    i += 1
print(div)
