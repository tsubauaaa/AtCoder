S = input()
T = input()

S += "!"
length = len(T)

ans = 0
for s, t in zip(S, T):
    ans += 1
    if s != t:
        break

print(ans)