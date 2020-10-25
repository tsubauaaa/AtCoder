N = input()
q = len(N)
ans = (q - 1) * 9
ans += int(N[0]) - 1
print(max(ans, sum([int(n) for n in N])))
