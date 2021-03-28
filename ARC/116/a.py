T = int(input())
for i in range(T):
    case = int(input())
    if (case + 2) % 4 == 0:
        print("Same")
        continue
    if case % 2 == 0:
        print("Even")
    else:
        print("Odd")
