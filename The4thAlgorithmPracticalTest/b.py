X, Y = map(int, input().split())

if Y == 0:
    print("ERROR")
    exit()

ans = str(X / Y).split(".")[0] + "."

if len(str(X / Y).split(".")[1]) < 2:
    ans += str(X / Y).split(".")[1] + "0"
else:
    ans += str(X / Y).split(".")[1][:2]

print(ans)
