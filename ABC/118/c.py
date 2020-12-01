N = int(input())
A = list(map(int, input().split()))
min_A = min(A)
AA = [a for a in A if a % min_A != 0]
print(AA)
if len(AA) == 0:
    print(min_A)
else:
    if sum(AA) % min_A == 0:
        print(min_A)
    else:
        print(sum(AA) % min_A)
