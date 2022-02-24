S = input()
odd = 0
even = 0
for i in range(0, len(S) - 1):
    if (i + 1) % 2 != 0:
        odd += int(S[i])
    else:
        even += int(S[i])

print("Yes" if (odd * 3 + even) % 10 == int(S[-1]) else "No")
