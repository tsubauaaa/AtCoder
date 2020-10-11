if __name__ == "__main__":
    N, Y = map(int, input().split())
    ans10000 = -1
    ans5000 = -1
    ans1000 = -1
    for x in range(N + 1):
        for y in range(N + 1):
            z = N - x - y
            if z < 0:
                continue
            if 10000 * x + 5000 * y + 1000 * z == Y:
                ans10000 = x
                ans5000 = y
                ans1000 = z
    print(f"{ans10000} {ans5000} {ans1000}")
