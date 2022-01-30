N = list(map(int, input().split()))
confirms = [1, 7, 9, 4]
for n in N:
    if n in confirms:
        confirms.remove(n)

print("YES" if confirms == [] else "NO")
