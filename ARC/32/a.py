n = int(input())
if n == 1:
    print("BOWWOW")
    exit()
s = n * (n + 1) // 2
for p in range(2, s):
    if s % p == 0:
        print("BOWWOW")
        exit()
print("WANWAN")
