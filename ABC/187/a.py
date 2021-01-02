A, B = input().split()
sum_A = 0
sum_B = 0
for i in range(3):
    sum_A += int(A[i])
    sum_B += int(B[i])
print(max(sum_A, sum_B))
