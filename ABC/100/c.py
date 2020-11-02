N = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    a.sort(reverse=True)
    print(a)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(N):
        if a[i] > 10 ** 9:
            cnt1 += 1

        if a[i] % 2 == 0 and cnt2 == 0:
            a[i] = a[i] / 2
            cnt2 += 1
        else:
            a[i] = a[i] * 3

    if cnt2 == 0 or cnt1 > 0:
        break

    ans += 1

while True:
    a.sort(reverse=True)
    print(a)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(N):
        if a[i] > 10 ** 9:
            cnt1 += 1

        if a[i] % 2 == 0 and cnt2 == 0:
            a[i] = a[i] / 2
            cnt2 += 1
        else:
            a[i] = a[i] * 3

    if cnt2 == 0 or cnt1 > 0:
        break

    ans += 1

print(ans)
