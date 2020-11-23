def is_available(r1, c1, r2, c2):
    for i in range(r1 - 5, r1 + 6):
        for j in range(c1 - 5, c1 + 6):
            if r1 + c1 == i + j or r1 - c1 == i - j or abs(r1 - i) + abs(c1 - j) <= 3:
                if i == r2 and j == c2:
                    return True
    return False


r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
if r1 == r2 and c1 == c2:
    print(0)
    exit()

print(r1 + c1 - (r2 + c2))
print(r1 - c1 - (r2 - c2))
