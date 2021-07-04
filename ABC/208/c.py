N, K = map(int, input().split())
a = list(map(int, input().split()))
a_dic = {a[i]: [i + 1] for i in range(N)}
a_sorted = sorted(a)
a_sorted_dic = {a_sorted[i]: [i + 1] for i in range(N)}

for ai in a:
    a_dic[ai].append(a_sorted_dic[ai][0])
ans = [0] * N
all = K // N
less = K % N

for k, v in a_dic.items():
    if v[1] <= less:
        print(all + 1)
    else:
        print(all)
