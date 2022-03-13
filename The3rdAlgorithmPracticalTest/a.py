s = input()
t = input()

same = True
insentive = True

for i in range(len(s)):
    S = s[i].upper()
    T = t[i].upper()
    if s[i] != t[i]:
        same = False
        if S != T:
            insentive = False

if same:
    print("same")
    exit()

print("case-insensitive" if insentive else "different")
