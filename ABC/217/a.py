S, T=input().split()
lst = [S,T]
lst.sort()

S_index = lst.index(S)
T_index = lst.index(T)

if S_index < T_index:
    print("Yes")
else:
    print("No")

