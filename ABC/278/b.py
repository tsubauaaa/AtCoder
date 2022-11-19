H, M = map(int, input().split())

times = []
miss_times = []

for i in range(24):
    for j in range(60):
        if i < 10:
            A = "0"
            B = str(i)
        else:
            A = str(i)[0]
            B = str(i)[1]

        if j < 10:
            C = "0"
            D = str(j)
        else:
            C = str(j)[0]
            D = str(j)[1]
        times.append(A + B + C + D)
        miss_times.append(A + C + B + D)

ans = []

for mt in miss_times:
    if mt in times:
        ans.append(mt)

if H < 10:
    A = "0"
    B = str(H)
else:
    A = str(H)[0]
    B = str(H)[1]

if M < 10:
    C = "0"
    D = str(M)
else:
    C = str(M)[0]
    D = str(M)[1]

time = A + B + C + D

index = times.index(time)

for time in times[index:]:
    if time in ans:
        if time[0] == "0":
            h = time[1]
        else:
            h = time[:2]
        if time[2] == "0":
            m = time[3]
        else:
            m = time[2:]
        print(h, m)
        exit()


for time in times[:index]:
    if time in ans:
        if time[0] == "0":
            h = time[1]
        else:
            h = time[:2]
        if time[2] == "0":
            m = time[3]
        else:
            m = time[2:]
        print(h, m)
        exit()
