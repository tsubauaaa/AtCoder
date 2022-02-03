H1, M1, H2, M2, K = map(int, input().split())

m = (H2 - H1) * 60 + M2 - M1

print(max(0, m - K))
