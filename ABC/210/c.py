N,K=map(int,input().split())
c = list(map(int,input().split()))
def cumsum(xs):
  result = [xs[0]]
  for x in xs[1:]:
    result.append(result[-1] + x)
  return result

csum = cumsum(c)
print(csum)
ans = 0
for i in range(N-K+1):
    print(csum[i+K-1] - csum[i])

