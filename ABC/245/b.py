N = int(input())
A = list(set(map(int, input().split())))
A.sort()
A_max = A[-1]

for i in range(A_max + 2):
    if i not in A:
        print(i)
        exit()
