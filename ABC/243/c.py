N = int(input())
XY = {}
for i in range(N):
    x, y = map(int, input().split())
    XY[i] = (x, y)
S = input()
XY = dict(sorted(XY.items(), key=lambda x: x[1][0]))

Y = {}

for k, v in XY.items():
    if v[1] in Y:
        Y[v[1]].append(k)
    else:
        Y[v[1]] = [k]

# yが一緒でかつxが小さい方がR、xが大きい方がLのものを探す

for k, v in Y.items():
    len_v = len(v)
    if len_v == 1:
        continue
    if len_v > 1:
        R = False
        for i in range(len_v):
            # print(XY[v[i]], S[v[i]])
            if S[v[i]] == "R":
                R = True
            if R and S[v[i]] == "L":
                print("Yes")
                exit()

print("No")
