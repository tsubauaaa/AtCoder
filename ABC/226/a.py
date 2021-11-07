X = input()

if int(X.split(".")[1][0]) > 4:
    print(int(X.split(".")[0]) +1)
else:
    print(int(X.split(".")[0]))