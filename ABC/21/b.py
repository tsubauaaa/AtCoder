N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
P.insert(0, a)
P.append(b)
if len(set(P)) != K + 2:
    print("NO")
else:
    print("YES")
