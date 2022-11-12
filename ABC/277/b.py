N = int(input())
ans = True
S = []
for i in range(N):
    s = input()
    if s[0] not in ("H", "D", "C", "S"):
        ans = False
    if s[1] not in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"):
        ans = False
    S.append(s)

if ans:
    if len(list(set(S))) != N:
        print("No")
    else:
        print("Yes")
else:
    print("No")
