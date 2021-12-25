import itertools

N, X = map(int, input().split())

Ls = []
for i in range(N):
    La = list(map(int, input().split()))
    Ls.append(La[1:])

ans = 0
for p in list(itertools.product(*Ls)):
    calc = 1
    for pi in p:
        calc *= pi
    if calc == X:
        ans += 1

print(ans)
