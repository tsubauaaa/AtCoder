A, B, C, K = map(int, input().split())
ans = 0
if A > K:
    print(K)
    exit()
else:
    ans += 1 * A
    K -= A
    if B > K:
        ans += 0 * K
        print(ans)
        exit()
    else:
        ans += 0 * B
        K -= B
        if C > K:
            ans += -1 * K
            print(ans)
            exit()
        else:
            ans += -1 * C
            K -= C
print(ans)
