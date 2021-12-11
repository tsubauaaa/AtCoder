N = int(input())

S = [input() for _ in range(N)]

S_dic = {x: 1 for x in set(S)}

for i in range(N):
    S_dic[S[i]] += 1
    
print(max(S_dic, key=S_dic.get))