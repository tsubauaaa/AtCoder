N = int(input())
A = list(map(int, input().split()))
boss = [0] * N

for i in range(len(A)):
    boss[A[i] - 1] += 1

for b in boss:
    print(b)
