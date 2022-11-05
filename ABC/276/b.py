N, M = map(int, input().split())

ans = {i + 1: [[0], []] for i in range(N)}

for i in range(M):
    A, B = map(int, input().split())
    ans[A][1].append(B)
    ans[A][0][0] += 1
    ans[B][1].append(A)
    ans[B][0][0] += 1

for k, v in ans.items():
    if v[0][0] == 0:
        print(0)
        continue
    cnt = v[0]
    sorted_v = sorted(v[1])
    cnt.extend(sorted_v)
    print(*cnt)
