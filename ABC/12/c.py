N = int(input())
remain = 2025 - N
ans = []
i = 1
while i * i <= remain:
    if remain % i == 0:
        if i < 10 and remain // i < 10:
            ans.append([i, remain // i])
            if i != remain // i:
                ans.append([remain // i, i])
    i += 1
ans.sort()
for ai in ans:
    print(f"{ai[0]} x {ai[1]}")
