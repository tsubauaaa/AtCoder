N = int(input())
L = list(map(int, input().split()))
L.sort()

print("Yes" if L[-1] < sum(L[:-1]) else "No")


