S = list(input())
T = list(input())

misses = 0

for s, t in zip(S, T):
    if s != t:
        misses += 1

print("Yes" if misses != 2 else "No")

