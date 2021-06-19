import math
N = int(input())
ans = ""
if math.floor(N * 1.08) < 206:
    ans = 'Yay!'
elif math.floor(N * 1.08) == 206:
    ans = 'so-so'
else:
    ans = ':('
print(ans)
