Q, H, S, D = map(int, input().split())
N = int(input())

one = min(4 * Q, 2 * H, S)
two = D

print(min(N // 2 * two + N % 2 * one, N // 1 * one))
