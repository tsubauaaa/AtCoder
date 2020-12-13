W = int(input())
S = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
ans = ""
for i in range(1, len(S) + 1):
    ans += ans.join(S[i - 1])
    if i % W == 0:
        ans += "\n"
print(ans.strip())
