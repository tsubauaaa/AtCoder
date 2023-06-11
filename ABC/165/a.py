K = int(input())
A, B = map(int, input().split())

ans = False

for i in range(1, 1001, 1):
    if A <= i*K <= B:
        ans = True

print("OK" if ans else "NG")
