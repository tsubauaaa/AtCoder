W, a, b = map(int, input().split())
print(a, a + W, b, b + W)

if b < a + W and a + W < a + W:
    print(a + W - b)
elif a < b and b + W < a:
    print(b - a)
else:
    print(0)
