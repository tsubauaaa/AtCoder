S = list(input())
N = int(input())
for _ in range(N):
    left, right = map(int, input().split())
    sub = S[left - 1 : right]
    sub.reverse()
    S = S[: left - 1] + sub + S[right:]
print("".join(S))
