S = input()

YYMMs = []
MMYYs = []

for i in range(100):
    YY = str(i) if len(str(i)) != 1 else "0" + str(i)
    for j in range(1,13):
        MM = str(j) if len(str(j)) != 1 else "0" + str(j)
        YYMMs.append(YY+MM)

for i in range(1, 13):
    YY = str(i) if len(str(i)) != 1 else "0" + str(i)
    for j in range(100):
        MM = str(j) if len(str(j)) != 1 else "0" + str(j)
        MMYYs.append(YY+MM)

if S in YYMMs:
    if S in MMYYs:
        print("AMBIGUOUS")
    else:
        print("YYMM")
elif S in MMYYs:
    print("MMYY")
else:
    print("NA")