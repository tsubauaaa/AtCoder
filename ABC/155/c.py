N = int(input())
d = {}

for i in range(N):
    S = input()
    if S in d:
        d[S] += 1
    else:
        d[S] = 1

max_val = max(d.values())
keys_of_max_val = [key for key in d if d[key] == max_val]

keys_of_max_val.sort()

for i in range(len(keys_of_max_val)):
    print(keys_of_max_val[i])
