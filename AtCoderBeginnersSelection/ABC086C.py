if __name__ == "__main__":
    N = int(input())
    td = 0
    xd = 0
    yd = 0
    ans = 0
    for i in range(N):
        t, x, y = map(int, input().split())
        distance = abs(x-xd)+abs(y-yd)
        steps = t-td

        if steps >= distance and (steps-distance)%2 == 0:
            ans += 1
        td = t
        xd = x
        yd = y
    
    if ans == N:
        print('Yes')
    else:
        print('No')
        