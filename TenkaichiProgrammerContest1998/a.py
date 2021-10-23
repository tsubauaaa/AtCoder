ans = [100, 100, 200]
for i in range(2, 19):
    ans.append(ans[i + 1 - 1] + ans[i + 1 - 2] + ans[i + 1 - 3])
print(ans[-1])