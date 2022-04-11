N = int(input())

S = []
T = []

for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

for i in range(N):
    s_cnt = 0
    t_cnt = 0
    s_cnt += S.count(S[i])
    s_cnt += T.count(S[i])
    t_cnt += S.count(T[i])
    t_cnt += T.count(T[i])
    s_cnt -= 1
    t_cnt -= 1

    if S[i] == T[i]:
        s_cnt -= 1
        t_cnt -= 1

    if not (s_cnt == 0 or t_cnt == 0):
        print("No")
        exit()


print("Yes")
