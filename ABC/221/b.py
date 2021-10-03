S=input()
T=input()

if S == T:
    print("Yes")
    exit()

for i in range(1, len(S)):
    target=S[:i-1]+S[i]+S[i-1]+S[i+1:]
    if target == T:
        print("Yes")
        exit()
print("No")