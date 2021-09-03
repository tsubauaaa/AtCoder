S = input()

num = S[0]

for s in S[1:]:
    if num == s:
        print("Bad")
        exit()
    num = s
print("Good")