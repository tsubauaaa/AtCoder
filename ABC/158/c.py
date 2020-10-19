import sys

A, B = map(float, input().split())

for i in range(10000):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        sys.exit()

print(-1)
