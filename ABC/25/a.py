S = input()
N = int(input())
ans = []
for s1 in S:
    for s2 in S:
        ans.append(s1 + s2)
ans.sort()
print(ans[N - 1])
