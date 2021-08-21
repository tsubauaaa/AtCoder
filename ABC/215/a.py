S = input()
ans = "Hello,World!"

if len(S) != len(ans):
    print("WA")
    exit()

for i in range(len(ans)):
    if ans[i] != S[i]:
        print("WA")
        exit()
print("AC")
