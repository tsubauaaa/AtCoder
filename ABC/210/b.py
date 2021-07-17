N=int(input())
S=input()

for i in range(N):
    if S[i] == "1":
        break
print("Takahashi" if i % 2 == 0 else "Aoki")
