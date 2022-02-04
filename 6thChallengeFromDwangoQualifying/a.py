N = int(input())
st = []
for i in range(N):
    s, t = input().split()
    st.append((s, int(t)))
X = input()
ans = 0
index = 0
isSleep = False
for i in range(N):
    if st[i][0] == X:
        isSleep = True
        index = i
    if isSleep:
        ans += st[i][1]

print(ans - st[index][1])

