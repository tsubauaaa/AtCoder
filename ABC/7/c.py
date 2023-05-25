from collections import deque

R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
S = []
for _ in range(R):
    S.append(input())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点からの最小移動回数を管理する2次元配列。-1であれば未訪問。
dist = [[-1]*C for _ in range(R)]

# キューを用意して始点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

# キューから取り出しながら探索する
while len(Q) > 0:
    i, j = Q.popleft()
    # 4つの隣マスを確認する
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # もし盤面の範囲内でなければ無視する
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue
        # もし壁マスであれば無視する
        if S[i][j] == '#':
            continue
        # もし未訪問(dist[i2][j2]が-1)であれば距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

# 始点から終点までの最小移動回数を出力
print(dist[gy][gx])
