S = input()

ans1 = [False] * 2
ans2 = {s: 0 for s in S}

for s in S:
    ans2[s] += 1
    if s.islower():
        ans1[0] = True
        continue
    if s.isupper():
        ans1[1] = True

if sum(ans1) != 2:
    print("No")
    exit()

for k, v in ans2.items():
    if v > 1:
        print("No")
        exit()

print("Yes")
