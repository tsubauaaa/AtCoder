K=int(input())
A,B=map(int,input().split())

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out

A_ans = Base_n_to_10(str(A),K)
B_ans = Base_n_to_10(str(B),K)

print(A_ans*B_ans)