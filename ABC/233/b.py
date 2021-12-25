L, R = map(int, input().split())
S = input()
T = S[L - 1 : R]
rT = T[::-1]
print(S[: L - 1] + rT + S[R:])
