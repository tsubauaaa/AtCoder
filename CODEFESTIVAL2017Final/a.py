S = input()
if S[0] != "A":
    ans = "A"
else:
    ans = ""
for i in range(len(S)):
    ans += ans.join(S[i])
    if i < len(S) - 1:
        if (S[i] == "H" and S[i + 1] != "A") or (S[i] == "B" and S[i + 1] != "A"):
            ans += ans.join("A")
if ans[-1] != "A":
    ans += ans.join("A")
print("YES" if ans == "AKIHABARA" else "NO")
