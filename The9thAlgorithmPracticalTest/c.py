N = int(input())
problems = {"A": [""], "B": [""], "C": [""], "D": [""], "E": [""], "F": [""]}

for i in range(N):
    P, V = input().split()
    if V == "WA":
        continue
    else:
        if problems[P][0] == "":
            problems[P][0] = V
            problems[P].append(i + 1)
        else:
            continue

for k, v in problems.items():
    print(v[1])
