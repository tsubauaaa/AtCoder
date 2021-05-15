N = int(input())
ans = {}
T_list = []
for i in range(N):
    S, T = input().split()
    ans[T] = S
    T_list.append(int(T))
T_list.sort(reverse=True)
print(ans[str(T_list[1])])
