S = input()
possibles = []
impossibles = []
unknown = []
for i in range(len(S)):
    if S[i] == "o":
        possibles.append(str(i))
    elif S[i] == "x":
        impossibles.append(i)
    else:
        unknown.append(str(i))
ans = 0
for i in range(10000):
    num = str(i).zfill(4)
    p_cnt = 0
    in_p_cnt = 0
    u_cnt = 0
    in_u_cnt = 0
    for p in possibles:
        if p in num:
            p_cnt += 1
            in_p_cnt += num.count(p)
    if p_cnt != len(possibles):
        continue
    for u in unknown:
        if u in num:
            u_cnt += 1
            in_u_cnt += num.count(u)
    if in_p_cnt + in_u_cnt != 4:
        continue
    ans += 1
print(ans)
