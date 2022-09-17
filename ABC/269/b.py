w_start = 0
h_start = 0
w_cnt = 0
h_cnt = 0
for i in range(10):
    S = input()
    is_first = False
    for j in range(10):
        if S[j] == "#":
            if not is_first:
                w_start = j
                h_start = i
                is_first = True
            w_cnt += 1

    if is_first:
        h_cnt += 1

print(h_start + 1 - (h_cnt - 1), h_start + 1)
print(w_start + 1, w_start + w_cnt // h_cnt)
