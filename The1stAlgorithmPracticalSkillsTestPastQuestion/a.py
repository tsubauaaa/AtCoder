S = input()

for s in S:
    if not s.isdecimal():
        print("error")
        exit()

print(int(S) * 2)
