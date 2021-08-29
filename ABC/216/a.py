X,Y=input().split(".")

X = int(X)
Y=int(Y)

if 0<=Y<=2:
    print(f"{X}-")
elif 3<=Y<=6:
    print(X)
else:
    print(f"{X}+")