import sys

def division(a, b, c):
    return (b+c)/2, (a+c)/2, (a+b)/2

A, B, C = map(int, input().split())
ans = 0
while True:
    if A%2 != 0 or B%2 != 0 or C%2 != 0:
        break
    elif A == B == C:
        ans = -1
        break
    ans += 1
    A, B, C = division(A, B, C)
    
    
print(ans)