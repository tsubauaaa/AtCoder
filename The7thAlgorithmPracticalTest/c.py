S = input()
L, R = map(int, input().split())

if S == "0":
    if L <= int(S) <= R:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if S[0] != "0" and L <= int(S) <= R:
    print("Yes")
else:
    print("No")
