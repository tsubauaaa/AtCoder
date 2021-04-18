A, B = map(int, input().split())

a_ans = set([i for i in range(1, A + 1)])
b_ans = set([i for i in range(1, B + 1)])
ans = []
if A < B:
    b_ans_nega = [-1 * b for b in list(b_ans)]
    a_ans_part = list(a_ans)[1:]
    tmp = sum(b_ans - a_ans) + list(a_ans)[0]
    a_ans_part.append(tmp)
    ans = a_ans_part + b_ans_nega
    print(*ans)
elif A > B:
    b_ans_nega = [-1 * b for b in list(b_ans)]
    b_ans_nega_part = list(b_ans_nega)[1:]
    tmp = sum(a_ans - b_ans) - list(b_ans_nega)[0]
    b_ans_nega_part.append(-1 * tmp)
    ans = b_ans_nega_part + list(a_ans)
    print(*ans)
else:
    b_ans_nega = [-1 * b for b in list(b_ans)]
    ans = list(a_ans) + b_ans_nega
    print(*ans)

# pos_cnt = 0
# nega_cnt = 0
# sum_ans = 0
# for ansi in ans:
#     if ansi > 0:
#         pos_cnt += 1
#     else:
#         nega_cnt += 1
#     sum_ans += ansi
# print(pos_cnt, nega_cnt, sum_ans)
