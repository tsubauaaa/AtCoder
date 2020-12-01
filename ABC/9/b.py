N = int(input())
menu = [int(input()) for _ in range(N)]
print(sorted(set(menu))[-2])
