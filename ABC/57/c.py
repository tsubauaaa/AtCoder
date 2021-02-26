def F(A, B):
    digit_A = len(str(A))
    digit_B = len(str(B))
    return max(digit_A, digit_B)


N = int(input())
i = 1
ans = len(str(N)) + 1
while i * i <= N:
    if N % i == 0:
        ans = min(F(i, N // i), ans)
    i += 1
print(ans)
