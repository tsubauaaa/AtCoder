n = int(input())
sequences = [0, 0, 1]

for i in range(3, 10 ** 6 + 1):
    next = (sequences[i - 1] + sequences[i - 2] + sequences[i - 3]) % 10007
    sequences.append(next)

print(sequences[n - 1])
