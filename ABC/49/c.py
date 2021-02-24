S = input()
S = S[::-1]
while len(S) > 0:
    if S[:7] == "remaerd":
        S = S[7:]
    elif S[:6] == "resare":
        S = S[6:]
    elif S[:5] in ("maerd", "esare"):
        S = S[5:]
    else:
        print("NO")
        exit()
print("YES")
