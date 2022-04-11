N = int(input())
Si = "1"
for i in range(N - 1):
    Si = Si + " " + str(i + 2) + " " + Si

print(Si)
