S = list(input())

string = ""
prev = ""
ans = 0

for s in S:
    string += s
    if string != prev:
        ans += 1
        string, prev = "", string
print(ans)
