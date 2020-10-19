O = input()
E = input()
ans = ""
for i in range(len(O)):
    ans += O[i]
    if i == len(O) - 1 and len(O) > len(E):
        break
    else:
        ans += E[i]

print(ans)
