H, W, N = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


def calculate_rank(vector):
    a = {}
    rank = 1
    for num in sorted(vector):
        if num not in a:
            a[num] = rank
            rank = rank + 1
    return [a[i] for i in vector]


ans_A = calculate_rank(A)
ans_B = calculate_rank(B)

for a, b in zip(ans_A, ans_B):
    print(f"{a} {b}")
