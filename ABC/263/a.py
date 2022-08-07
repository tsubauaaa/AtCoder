cards = list(map(int, input().split()))

counts = {}

for card in cards:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1

exists_three = False
exists_two = False
for k, v in counts.items():
    if v == 3:
        exists_three = True
    elif v == 2:
        exists_two = True
    if exists_three and exists_two:
        print("Yes")
        exit()
print("No")
