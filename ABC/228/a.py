S,T,X = map(int, input().split())

if T < S:
    T = T + 24

if X < S:
    X = X + 24
    
if S <= X+0.5 <= T:
    print("Yes")
else:
    print("No")