N = int(input())
A = list(map(int, input().split()))
odd = 0
for a in A:
    if a % 2 == 1:
        odd += 1
even = N - odd

odd_r = odd % 2
even_r = even % 2

print("YES" if odd_r == 0 else "NO")

