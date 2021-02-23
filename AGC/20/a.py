N, A, B = map(int, input().split())
ans = [True, True]
while True:
    if not ans[0] or not ans[1]:
        break
    if A + 1 != B:
        A += 1
    else:
        A -= 1
    if B - 1 != A:
        B -= 1
    else:
        B += 1
    if A in (0, B, N + 1):
        ans[0] = False
    elif B in (0, A, N + 1):
        ans[1] = False
if ans[0]:
    print("Alice")
elif ans[1]:
    print("Borys")
else:
    print("Draw")
