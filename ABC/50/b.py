N = int(input())
T = list(map(int, input().split()))
M = int(input())
for i in range(M):
    P, X = map(int, input().split())
    org_T = T[P - 1]
    T[P - 1] = X
    print(sum(T))
    T[P - 1] = org_T
