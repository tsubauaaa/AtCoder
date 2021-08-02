groups = list(map(int, input().split()))

print("Yes" if len(set(groups)) == 2 else "No")
