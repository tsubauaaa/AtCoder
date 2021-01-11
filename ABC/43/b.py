s = list(input())
ans = []
len_s = len(s)
for i in range(len_s):
    if s[i] == "0":
        ans.append("0")
    elif s[i] == "1":
        ans.append("1")
    else:
        if len(ans) != 0:
            del ans[-1]
print("".join(ans))
