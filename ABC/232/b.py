S = input()
T = input()

alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)] * 2

for i in range(1, 27):
    for s, t in zip(S, T):
        shift_index = alphabets.index(s) + i
        if alphabets[shift_index] != t:
            break
    else:
        print("Yes")
        exit()

print("No")
