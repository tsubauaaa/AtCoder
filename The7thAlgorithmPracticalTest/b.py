A, B, C = map(int, input().split())

while A > B * C:
    A -= 1

print(A / B)
