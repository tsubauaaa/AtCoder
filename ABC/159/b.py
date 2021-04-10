S = input()
N = len(S)
T = S[0 : (N - 1) // 2]
U = S[(N + 3) // 2 - 1 : N]

if S == S[::-1] and T == T[::-1] and U == U[::-1]:
    print("Yes")
else:
    print("No")
