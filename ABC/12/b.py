N = int(input())
h = N // 3600
m = (N - 3600 * h) // 60
s = N - 3600 * h - 60 * m
h = str(h) if h > 9 else "0" + str(h)
m = str(m) if m > 9 else "0" + str(m)
s = str(s) if s > 9 else "0" + str(s)
print(f"{h}:{m}:{s}")
