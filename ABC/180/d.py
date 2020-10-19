X, Y, A, B = map(int, input().split())
strong = X
exp = 0
while strong < B:
    strong *= A
    exp += 1

if strong == B:
    strong /= A
    exp -= 1

n = (Y - strong) // B

print(int(n + exp))
