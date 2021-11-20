N,K=map(int,input().split())

scores = {i: 0 for i in range(N)}

for i in range(N):
    scores[i] = sum(list(map(int,input().split())))

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# print(scores)
# print(sorted_scores)
ans = ["No"] * N
target = sorted_scores[K-1][1]
for i, score in enumerate(sorted_scores):
    if i > K:
        if target <= score[1]+300:
            ans[score[0]] = "Yes"
    else:
        ans[score[0]] = "Yes"

for ansi in ans:
    print(ansi)