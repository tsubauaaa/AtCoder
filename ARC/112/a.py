from scipy.special import comb

T = int(input())
# cases = [(0, 0) for _ in range(T)]
cases = tuple(map(int, input().split()))
div = []
i = 1
while i * i <= cases[1]:
    if cases[1] % i == 0:
        div.append(i)
        div.append(cases[1] // i)
    i += 1
div2 = []
print(len(div))
j = 1
while j * j <= cases[0]:
    if cases[0] % j == 0:
        div2.append(j)
        div2.append(cases[0] // j)
    j += 1
print(len(div2))


# for i in range(T):
#     cases[i] = tuple(map(int, input().split()))
#     # a = comb(cases[i][1] - cases[i][0], 3, exact=True, repetition=True)
#     a = comb(6, 3, exact=True)

#     print(a)
