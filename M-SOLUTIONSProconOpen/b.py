S = input()

cnt = 0

for s in S:
    if s == "o":
        cnt += 1

print("YES" if cnt + (15 - len(S)) >= 8 else "NO")
