N = int(input())
W = list(map(str, input().split()))
ans = 0
for w in W:
    w = w.replace(".", "")
    if w == "TAKAHASHIKUN" or w == "Takahashikun" or w == "takahashikun":
        ans += 1
print(ans)
