V, A, B, C = map(int, input().split())
S = [A, B, C]
i = 0
while True:
    V -= S[i]
    if V < 0:
        break
    if i == 2:
        i = 0
    else:
        i += 1
if i == 0:
    print("F")
elif i == 1:
    print("M")
else:
    print("T")
