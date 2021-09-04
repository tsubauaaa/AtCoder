L, Q = map(int, input().split())
line = [i+1 for i in range(L)]
cuts = {}
for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        line.insert(x, 0)
    cuts[i] = line

    print(cuts)

# for i in range(Q):
#     c, x = map(int,input().split())        