import itertools

N, M = map(int, input().split())
takahashi = {i + 1: [] for i in range(N)}
aoki = {i + 1: [] for i in range(N)}
nums = [i + 1 for i in range(N)]
perms = itertools.permutations(nums)
for i in range(M):
    A, B = map(int, input().split())
    takahashi[A].append(B)
    takahashi[B].append(A)

for i in range(M):
    C, D = map(int, input().split())
    aoki[C].append(D)
    aoki[D].append(C)

takahashi = {k: list(set(sorted(v))) for k, v in takahashi.items()}

sorted_takahashi = sorted(takahashi.items())

for perm in perms:
    target = {}
    for k, v in aoki.items():
        tv = []
        for vv in v:
            tv.append(perm[vv - 1])
        target[perm[k - 1]] = sorted(tv)

    if sorted_takahashi == sorted(target.items()):
        print('Yes')
        exit()

print("No")
