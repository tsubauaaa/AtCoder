import math

N,D=map(int,input().split())

range = (2*D)+1

print(math.ceil(N/range))
