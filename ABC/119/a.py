S = input()

month = int(S[6:7]) if S[5:6] == "0" else int(S[5:7])
if month >= 5:
    print("TBD")
else:
    print("Heisei")