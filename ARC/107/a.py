A, B, C = map(int, input().split())

ans = (A*(A+1)//2) * (B*(B+1)//2) * (C*(C+1)//2)

print(ans % 998244353)
