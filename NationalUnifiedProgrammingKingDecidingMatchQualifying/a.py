N, A, B = map(int, input().split())
print(min(A, B), abs(min(0, N - (A + B))))
