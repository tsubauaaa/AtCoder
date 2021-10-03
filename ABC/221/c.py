import itertools
N=[i for i in input()]
len_N = len(N)
harf = len_N//2
ans = 0
for v in itertools.permutations(N):
    left = ""
    for l in v[:harf]:
        left += l
    right = ""
    for r in v[harf:]:
        right += r
    mul = int(left)*int(right)
    ans = max(ans, mul)

print(ans)



