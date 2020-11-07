from collections import Counter

S = input()

cnt = Counter(S)

for i in range(112, 1000, 8):
    # print(Counter(str(i)) - cnt)
    if not Counter(str(i)) - cnt:
        print(Counter(str(i)) - cnt)
        print("Yes")
        exit()

print("No")
