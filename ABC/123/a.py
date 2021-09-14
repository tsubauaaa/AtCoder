antenas = []
for _ in range(5):
    antenas.append(int(input()))

k = int(input())

for i in range(1, 5):
    for antena in antenas[:i]:
        if antenas[i] - antena > k:
            print(":(")
            exit()
print("Yay!")