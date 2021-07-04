import math
import itertools
P = int(input())
f = 1
i = 1
facts = []
while f <= P:
    f = math.factorial(i)
    if f > P:
        break
    facts.append(f)
    i += 1
facts.sort(reverse=True)

j = 0
ans = 0
while P != 0:
    P -= facts[j]
    if P < 0:
        P += facts[j]
        j += 1
        continue
    ans += 1

print(ans)
