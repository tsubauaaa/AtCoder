N = int(input())
A = list(map(int, input().split()))
X, x = max(A), min(A)
while X != x:
    A = [a - x if a == X else a for a in A]
    X, x = max(A), min(A)
print(X)
