if __name__ == "__main__":
    N, Y = map(int, input().split())
    ans10000 = -1
    ans5000 = -1
    ans1000 = -1
    for a in range(0, N+1):
        for b in range(0, N+1):
            c = N - a - b
            if c < 0:
                continue
            if a*10000 + b*5000 + c*1000 == Y:
                ans10000 = a
                ans5000 = b
                ans1000 = c

    print(f'{ans10000} {ans5000} {ans1000}')
    
