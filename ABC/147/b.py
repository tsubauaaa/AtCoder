S=input()
T=S[::-1]
ans =0 
for s,t in zip(S,T):
    if s != t:
        ans += 1
print(ans//2)