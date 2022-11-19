N = int(input())
A_list = list(map(int, input().split()))
A = {i + 1: a for i, a in enumerate(A_list)}
Q = int(input())
value = -1
ans = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        value = query[1]
        A = {}
    elif query[0] == 2:
        if (query[1]) not in A:
            A[query[1]] = value
        A[query[1]] += query[2]
    else:
        if (query[1]) not in A:
            A[query[1]] = value
        ans.append(A[query[1]])
for ai in ans:
    print(ai)