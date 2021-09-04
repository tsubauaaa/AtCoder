S1 = input()
S2 = input()
S3 = input()

cons = ["ABC", "ARC", "AGC", "AHC"]

for S in [S1,S2,S3]:
    cons.remove(S)

print(*cons)    