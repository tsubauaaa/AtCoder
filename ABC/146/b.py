N=int(input())
S = input()
ans = ""
for s in S:
    if ord(s)+N >= 91:
        code = 65+ord(s)+N - 91
    else:
        code = ord(s)+N
    ans += chr(code)
print(ans)