N=int(input())

names = []
for _ in range(N):
    S,T=input().split()
    names.append(f"{S} {T}")

M = len(set(names))

print("Yes" if M<N else "No")