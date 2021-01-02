N = int(input())
all_vote = [0] * N
all_aoki = 0
for i in range(N):
    a, t = map(int, input().split())
    all_vote[i] = (a + t, a, t)
    all_aoki += all_vote[i][1]
all_vote.sort(reverse=True)

print(all_vote, all_aoki)
