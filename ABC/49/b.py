H, W = map(int, input().split())
ans = []
for i in range(H):
    C = input()
    ans.append(C + "\n" + C)

for a in ans:
    print(a)
