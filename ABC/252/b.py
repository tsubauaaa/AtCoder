N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_delicious_size = max(A)
max_delicious_index = []
for i in range(N):
    if A[i] == max_delicious_size:
        max_delicious_index.append(i + 1)

for Bi in B:
    if Bi in max_delicious_index:
        print("Yes")
        exit()
print("No")
