X = input()
X_list = X.split("ch")
for x in X_list:
    if x == "":
        continue
    else:
        for xi in x:
            if xi not in ("o", "k", "u"):
                print("NO")
                exit()
print("YES")
