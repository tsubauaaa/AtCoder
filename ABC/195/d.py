import copy

N, M, Q = map(int, input().split())
baggages = []
for i in range(N):
    baggage = tuple(map(int, input().split()))
    baggages.append(baggage)
baggages = sorted(baggages, reverse=True, key=lambda x: x[1])
print(baggages)
X = list(map(int, input().split()))
print(X)
tmp_X = copy.deepcopy(X)
for i in range(Q):
    query = tuple(map(int, input().split()))
    del tmp_X[query[0] - 1 : query[1]]
    if len(tmp_X) == 0:
        print(0)
        continue
    ans = 0
    for j in range(len(tmp_X)):
        for k in range(N):
            if baggages[k][0] <= tmp_X[j]:
                ans += baggages[k][1]
                j += 1
    tmp_X = copy.deepcopy(X)
