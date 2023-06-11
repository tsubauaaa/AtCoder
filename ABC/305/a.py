import bisect

N = int(input())

waters = []

for i in range(101):
    if i % 5 == 0:
        waters.append(i)

index = bisect.bisect_left(waters, N)

if index == 0:
    print(waters[index])
else:
    if abs(N-waters[index]) < abs(N-waters[index-1]):
        print(waters[index])
    else:
        print(waters[index-1])
