s = input()
for s, r in zip(s, s[::-1]):
    if s == "*" or r == "*":
        continue
    if s != r:
        print("NO")
        exit()
print("YES")
