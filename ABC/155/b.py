N = int(input())
A = list(map(int, input().split()))
evens = []
for i in range(N):
    if A[i] % 2 == 0:
        evens.append(A[i])
for even in evens:
    if even % 3 == 0 or even % 5 == 0:
        continue
    else:
        print("DENIED")
        exit()

print("APPROVED")
