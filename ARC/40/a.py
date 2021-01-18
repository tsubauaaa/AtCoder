N = int(input())
t = 0
a = 0
for _ in range(N):
    S = input()
    for s in S:
        if s == "R":
            t += 1
        elif s == "B":
            a += 1

if t > a:
    print("TAKAHASHI")
elif a > t:
    print("AOKI")
else:
    print("DRAW")
N = int(input())
t = 0
a = 0
for _ in range(N):
    S = input()
    for s in S:
        if s == "R":
            t += 1
        elif s == "B":
            a += 1

if t > a:
    print("TAKAHASHI")
elif a > t:
    print("AOKI")
else:
    print("DRAW")
