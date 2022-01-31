import itertools

S = input()

# aが0個必要な時
if S == S[::-1]:
    print("Yes")
    exit()


archive = []
for c, g in itertools.groupby(S):
    archive.append([c, len(list(g))])

# 末が1個以上のa連続じゃなければNo
if archive[-1][0] != "a":
    print("No")
    exit()

T = S[: -1 * archive[-1][1]]

if archive[0][0] == "a":
    # 先頭も末もaがあるとして、aの個数が先頭の方が末より多い場合はNo
    if archive[0][1] > archive[-1][1]:
        print("No")
        exit()
    else:
        T = T[archive[0][1] :]

if T == T[::-1]:
    print("Yes")
else:
    print("No")
