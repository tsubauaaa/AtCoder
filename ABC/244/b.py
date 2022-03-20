N = int(input())
T = input()
dir = "E"
ans = (0, 0)

for i in range(N):
    if T[i] == "S":
        if dir == "N":
            ans = (ans[0], ans[1] + 1)
        elif dir == "S":
            ans = (ans[0], ans[1] - 1)
        elif dir == "E":
            ans = (ans[0] + 1, ans[1])
        else:
            ans = (ans[0] - 1, ans[1])
    else:
        if dir == "N":
            dir = "E"
        elif dir == "S":
            dir = "W"
        elif dir == "E":
            dir = "S"
        else:
            dir = "N"

print(ans[0], ans[1])
