N = int(input())
ans = []
for i in range(N):
    T = input()
    if (
        T.count("i") == 1
        and T.count("n") == 2
        and T.count("d") == 2
        and T.count("e") == 2
        and T.count("o") == 1
        and T.count("w") == 1
    ):
        ans.append("YES")
    else:
        ans.append("NO")
for i in range(N):
    print(ans[i])
