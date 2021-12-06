N = int(input())

if N < 10:
    zero = "00"
else:
    zero = "0"

print("AGC" +zero + str(N) if N < 42 else "AGC" + zero + str(N +1))