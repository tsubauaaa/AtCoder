N = int(input())
nums = []
for i in range(N):
    L = list(map(int,input().split()))
    nums.append(L[1:])

print(len(list(map(list, set(map(tuple, nums))))))
