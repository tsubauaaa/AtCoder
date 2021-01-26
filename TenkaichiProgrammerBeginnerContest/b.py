N = int(input())
min_A, min_B = map(int, input().split())
for i in range(1, N):
    A, B = map(int, input().split())
    if min_B > B:
        min_B = B
        min_A = A
print(min_A + min_B)
