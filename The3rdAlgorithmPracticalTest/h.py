N, L = map(int, input().split())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

# ハードルがある座標においてTrueとなるような配列
H = [False] * (L + 1)
for x in X:
    H[x] = True

# cost[i]:座標iで行動を終了するまでの最小所要時間
# 非常に大きな値で初期化しておきminを用いて更新する
cost = [10**100] * (L + 1)

# 初期条件
cost[0] = 0

# 順番に求めていく
for i in range(1, L + 1):
    # 行動1
    cost[i] = min(cost[i], cost[i - 1] + T[0])

    # 行動2
    if i >= 2:
        cost[i] = min(cost[i], cost[i - 2] + T[0] + T[1])

    # 行動3
    if i >= 4:
        cost[i] = min(cost[i], cost[i - 4] + T[0] + 3 * T[1])

    # もしハードルがあれば
    if H[i]:
        cost[i] += T[2]

# 答えは座標Lにぴったり止まるか、座標(L-3)〜(L-1)からジャンプ中にゴールしたもの
ans = cost[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, cost[i] + T[0] // 2 + T[1] * (2 * (L - i) - 1) // 2)

print(ans)
