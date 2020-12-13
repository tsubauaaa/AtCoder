S = input()
ans = S[0]
for i in range(1, len(S)):
    if i % 2 == 0:
        op = "+"
    else:
        op = "-"
    ans += op + S[i]
print(eval(ans))
