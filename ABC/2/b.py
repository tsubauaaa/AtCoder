W = input()
vowels = ["a", "i", "u", "e", "o"]

for vowel in vowels:
    W = W.replace(vowel, "")
print(W)
