S = input()
S += S.join("0")
splits = []
index = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        splits.append(S[index : i + 1])
        index = i + 1
ans = 0
for split in splits:
    n = len(split)
    if n != 1:
        ans += n * (n + 1) / 2
        print(n * (n + 1) / 2)

print(splits)
print(ans)
