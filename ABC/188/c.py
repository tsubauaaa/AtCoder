N = int(input())
A = list(map(int, input().split()))
M = 2 ** N
pairs = []
while len(A) > 2:
    for i in range(1, M - 1, 2):
        if A[i - 1] > A[i]:
            A[i] = 0
        else:
            A[i - 1] = 0
    A.remove(0)
    M = len(A)
    print(A)
print(min(A))
