W, a, b = map(int, input().split())
A = [i for i in range(a, a + W + 1)]
B = [i for i in range(b, b + W + 1)]
A.sort()
B.sort()
print(0 if len(set(A) & set(B)) != 0 else B[0] - A[-1] if a + W < b else A[0] - B[-1])
