if __name__ == "__main__":
    N = int(input())
    res = 0
    for n in range(1, N+1, 2):
        ans = 0
        for i in range(1, n+1):
            if n%i == 0:
                ans += 1
            if ans == 8:
                res += 1
    print(res)