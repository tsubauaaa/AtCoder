S = input()

days = [["Monday", 5], ["Tuesday", 4], ["Wednesday", 3], ["Thursday", 2], ["Friday", 1]]

for d in days:
    if d[0] == S:
        print(d[1])
        exit()
