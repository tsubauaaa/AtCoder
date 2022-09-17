import itertools

N = int(input())
N_2 = format(N, "b")
keta = len(N_2)
one_cnt = 0

for i in range(keta):
    if N_2[i] == "1":
        one_cnt += 1

patterns = []

for e in itertools.product([0, 1], repeat=one_cnt):
    patterns.append(e)
    one_index = -1
    tmp = ""
    for i in range(len(N_2)):
        if N_2[i] == "1":
            one_index += 1
            if e[one_index] == 0:
                s = "0"
            else:
                s = "1"
            tmp += s
        else:
            tmp += N_2[i]
    print(int(tmp, 2))
