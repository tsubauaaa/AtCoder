E = input().replace(" ", "")
B = input()
L = input().replace(" ", "")
match = 0
for i in range(len(L)):
    if E.find(L[i]) != -1:
        match += 1

if L.find(B) != -1:
    bonus = 1
else:
    bonus = 0

if match == 6:
    print(1)
elif match == 5 and bonus == 1:
    print(2)
elif match == 5:
    print(3)
elif match == 4:
    print(4)
elif match == 3:
    print(5)
else:
    print(0)
