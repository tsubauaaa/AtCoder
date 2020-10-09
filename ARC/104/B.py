N, S = map(str, input().split())
N = int(N)
ans = 0
for i in range(N):
    n = 0
    while True:
        if i+n > N:
            break
        T1 = S[i:i+n]
        if len(T1) == 0 or ('A' in T1 and T1.count('A') != T1.count('T')) or ('T' in T1 and T1.count('A') != T1.count('T')) or ('C' in T1 and T1.count('C') != T1.count('G')) or ('G' in T1 and T1.count('C') != T1.count('G')):
            n += 2
            continue      
        print(T1)
        ans += 1
        n += 2**(i+2)
 
print(ans)
