X, N = map(int, input().split())
P = list(map(int, input().split()))
nums = [i for i in range(0, 102)]
targets = list(set(nums) - set(P))
abss = [abs(targets[i] - X) for i in range(len(targets))]
min_index = abss.index(min(abss))
print(targets[min_index])
