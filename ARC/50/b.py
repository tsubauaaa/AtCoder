R, B = map(int, input().split())
x, y = map(int, input().split())

# X個の花束を作れるかをチェックする


def check(X):
    r = R - X
    b = B - X
    # 赤色、青色の花がどちらかX個なければ花束は作れない
    if r < 0 or b < 0:
        return False
    num = r // (x-1) + b // (y-1)

    return num >= X


ok = 0
ng = 10**18+1

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
