N, Q = map(int, input().split())

index = {}
ans = []
for i in range(N):
    index[i + 1] = i
    ans.append(i + 1)
for i in range(Q):
    x = int(input())
    right_index = index[x] + 1
    if right_index < N:
        right = ans[right_index]
        index[x] += 1
        index[right] -= 1
        ans[index[x]], ans[index[right]] = x, right
    else:
        left_index = index[x] - 1
        left = ans[left_index]
        index[x] -= 1
        index[left] += 1
        ans[index[x]], ans[index[left]] = x, left

print(*ans)
