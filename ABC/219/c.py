import sys

sys.setrecursionlimit(100000)

def is_than_smaller(x, l):
    L = min(len(x), len(l))
    for i in range(L):
        if x[i] != l[i]:
            x_o = X.index(x[i])
            l_o = X.index(l[i])
            if x_o < l_o:
                return True
            else:
                return False
    if len(x) < len(l):
        return True
    else:
        return False

    # if x < l:
    #     return True
    # else:
    #     return False
    
def is_than_bigger(x, l):
    L = min(len(x), len(l))
    for i in range(L):
        if x[i] != l[i]:
            x_o = X.index(x[i])
            l_o = X.index(l[i])
            if x_o >= l_o:
                return True
            else:
                return False
    if len(x) >= len(l):
        return True
    else:
        return False

    # if x >= l:
    #     return True
    # else:
    #     return False


def quicksort(lst):
    if not lst:
        return []
    
    return (quicksort([x for x in lst[1:] if is_than_smaller(x,lst[0])])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if is_than_bigger(x,lst[0])]))


def merge_sort(lst):
    # 再帰の終了条件
    if len(lst) == 0 or len(lst) == 1:
        return lst

    # 分割
    # 今の実装だと要素数が奇数の場合は余りの要素が後ろに入るが、どちらでもよいはず
    length = len(lst)
    firstHalf = lst[0:length // 2]
    latterHalf = lst[length // 2:length]

    # 再帰呼び出し。戻り値はソートされた状態になっている
    firstHalf = merge_sort(firstHalf)
    latterHalf = merge_sort(latterHalf)

    # マージ処理。それぞれの先頭要素を見て小さいほうからresultに詰めていけば全体がソートされたリストになる
    result = []
    while True:
        a = firstHalf[0]
        b = latterHalf[0]

        # 小さいほうをresultに追加し、元のリストからは削除
        # ここが逆なら降順ソートになる
        # if a < b:
        if is_than_smaller(a,b):
            result.append(a)
            firstHalf.pop(0)
        else:
            result.append(b)
            latterHalf.pop(0)

        # 両方とも空なら完了
        if len(firstHalf) == 0 and len(latterHalf) == 0:
            break

        # 片方だけ空なら、空じゃないほうをresultの後ろに足す
        if len(firstHalf) == 0:
            result +=  latterHalf
            break

        if len(latterHalf) == 0:
            result +=  firstHalf
            break

    return result

X = list(input())
N = int(input())
S = []
for _ in range(N):
    S.append(input())

ans = merge_sort(S)

for ansi in ans:
    print(ansi)