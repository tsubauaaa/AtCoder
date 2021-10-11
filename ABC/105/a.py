N, K = map(int, input().split())
participants = [0] * K

i = 0
while N > 0:
    participants[i] += 1
    N -= 1
    i += 1
    if i > K-1:
        i = 0
print(max(participants) - min(participants))
    