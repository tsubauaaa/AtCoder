S1 = input()
S2 = input()
S3 = input()
T = list(input())
S = [S1, S2,S3]

ans = ""

for t in T:
    ans += S[int(t)-1]

print(ans)