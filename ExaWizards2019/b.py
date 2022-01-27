N = int(input())
s = input()
Rs = 0
for i in range(N):
    if s[i] == "R":
        Rs += 1

print("Yes" if Rs > (N - Rs) else "No")
