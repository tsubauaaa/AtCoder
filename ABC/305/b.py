alphabets = "ABCDEFG"
distance = [0, 3, 4, 8, 9, 14, 23]
p, q = input().split()

s = alphabets.index(p)
e = alphabets.index(q)
print(abs(distance[e]-distance[s]))
