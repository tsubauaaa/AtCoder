N = input()
if N == N[::-1]:
    print("Yes")
    exit()
i = 0
for s in reversed(N):
    if s == "0":
        i += 1
    else:
        break
if i == 0:
    print("No")
    exit()
N = N[:-i]
print("Yes" if N == N[::-1] else "No")
