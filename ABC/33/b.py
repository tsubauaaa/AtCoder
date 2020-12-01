N = int(input())
towns = []
sum_P = 0
for i in range(N):
    S, P = map(str, input().split())
    towns.append([S, int(P)])
    sum_P += int(P)
for town in towns:
    if town[1] > sum_P / 2:
        print(town[0])
        exit()
else:
    print("atcoder")
