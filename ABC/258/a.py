K = int(input())

h = 21 + K // 60
m = K - 60 * (K // 60)

if m < 10:
    m = "0" + str(m)

print(f"{h}:{m}")
