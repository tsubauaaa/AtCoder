S = input()

ans = {"a": 0, "b": 0, "c": 0}

for s in S:
    ans[s] += 1

print(max(ans, key=ans.get))
