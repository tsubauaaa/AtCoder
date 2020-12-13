N, M, A, B = map(int, input().split())
for i in range(M):
    if N <= A:
        N += B
    c = int(input())
    N -= c
    if N < 0:
        print(i + 1)
        break
else:
    print("complete")
