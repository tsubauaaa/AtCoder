import collections

N = int(input())
A = list(map(int, input().split()))


for c in collections.Counter(A).most_common():
    if c[1] != 4:
        print(c[0])
        exit()
