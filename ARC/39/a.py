A, B = input().split()
ans_A = -2000
ans_B = -2000
for i in range(1, 10):
    ans_A = max(int(str(i) + A[1:]) - int(B), ans_A)
for i in range(10):
    ans_A = max(int(A[0] + str(i) + A[-1]) - int(B), ans_A)
for i in range(10):
    ans_A = max(int(A[:2] + str(i)) - int(B), ans_A)

for i in range(1, 10):
    ans_B = max(int(A) - int(str(i) + B[1:]), ans_B)
for i in range(10):
    ans_B = max(int(A) - int(B[0] + str(i) + B[-1]), ans_B)
for i in range(10):
    ans_B = max(int(A) - int(B[:2] + str(i)), ans_B)
print(max(ans_A, ans_B))
