A, B, C = map(int, input().split())

for i in range(min(A, B), max(A, B) + 1):
    if i == C:
        print("Yes")
        exit()
print("No")
