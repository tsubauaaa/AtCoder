N = int(input())
SA = []
for i in range(N):
    S, A = input().split()
    SA.append([int(A), S, i])

sorted_SA = sorted(SA)

first_index = sorted_SA[0][2]
for i in range(first_index, N+first_index):
    j = i
    if i > N-1:
        j = i-N
    print(SA[j][1])
