s = input()
k = int(input())

passwords = []

for i in range(len(s) - k + 1):
    passwords.append(s[i : i + k])

print(len(set(passwords)))
