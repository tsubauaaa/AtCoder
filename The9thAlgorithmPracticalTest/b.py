import bisect

N = int(input())
all_medals = [1, 5, 10, 50, 100, 500]
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    tsuri = B - A
    while tsuri > 1:
        if tsuri in all_medals:
            medal = all_medals[bisect.bisect_left(all_medals, tsuri)]
        else:
            medal = all_medals[bisect.bisect_left(all_medals, tsuri) - 1]

        tsuri -= medal
        if medal in [5, 50]:
            ans += 1
print(ans)
