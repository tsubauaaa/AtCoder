S = list(input())
set_S = set(S)

if len(set_S) != 2:
    print("No")
    exit()

if S.count(list(set_S)[0]) != 2:
    print("No")

print("Yes")