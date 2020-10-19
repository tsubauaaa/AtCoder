N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
diff_map = []
for i in range(N):
    diff = abs(A - (T - H[i] * 0.006))
    diff_map.append({"diff": diff, "num": i + 1})

ans = min(diff_map, key=lambda x: x["diff"])
print(ans["num"])
