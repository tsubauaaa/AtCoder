N, M = map(int,input().split())
rounds = [[] for _ in range(M)]

for i in range(2*N):
    A = list(input())
    for j in range(M):
        rounds[j].append(A[j])

scores = {i: 0 for i in range(2*N)}

for round in rounds:
    sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    ranks = [score[0] for score in sorted_scores]
    for i in range(0,2*N,2):
        hand1 = round[ranks[i]]
        hand2 = round[ranks[i+1]]
        if hand1 == "G" and hand2 == "C" :
            scores[ranks[i]] += 1
        if hand1 == "C" and hand2 == "P":
            scores[ranks[i]] += 1
        if hand1 == "P" and hand2 == "G":
            scores[ranks[i]] += 1
        if hand2 == "G" and hand1 == "C" :
            scores[ranks[i+1]] += 1
        if hand2 == "C" and hand1 == "P":
            scores[ranks[i+1]] += 1
        if hand2 == "P" and hand1 == "G":
            scores[ranks[i+1]] += 1

sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
ranks = [score[0] for score in sorted_scores]


for rank in ranks:
    print(rank+1)

