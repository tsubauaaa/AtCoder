def move(i, lim):
    if i == N:
        return
    for _ in range(i):
        cities[i - 1] -= lim
        cities[i] = lim
    i += 1
    print(cities, i)
    lim = int(input())
    move(i, lim)


N = int(input())
cities = [N] + [0] * (N - 1)
print(cities)
lim = int(input())
move(1, lim)
