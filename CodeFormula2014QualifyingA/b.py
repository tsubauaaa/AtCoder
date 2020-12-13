a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = ["x"] * 10

for i in range(len(p)):
    if p[i] == 0:
        ans[9] = "."
    else:
        ans[p[i] - 1] = "."

for i in range(len(q)):
    if q[i] == 0:
        ans[9] = "o"
    else:
        ans[q[i] - 1] = "o"

print(*ans[6:])
print(" ", end="")
print(*ans[3:6])
print("  ", end="")
print(*ans[1:3])
print("   ", end="")
print(*ans[0])
