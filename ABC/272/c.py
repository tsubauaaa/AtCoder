N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

evens = []
odds = []

for a in A:
    if a % 2 == 0:
        evens.append(a)
    else:
        odds.append(a)

if len(evens) <= 1 and len(odds) <= 1:
    print(-1)
    exit()

if len(evens) <= 1:
    max_evens = -1
else:
    max_evens = evens[0] + evens[1]

if len(odds) <= 1:
    max_odds = -1
else:
    max_odds = odds[0] + odds[1]

print(max(max_evens, max_odds))
