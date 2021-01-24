m = int(input())
km = m / 10 ** 3
if km < 0.1:
    vv = "00"
    print(vv)
elif 0.1 <= km <= 5:
    vv = int(km * 10)
    print(vv if len(str(vv)) == 2 else "0" + str(vv))
elif 6 <= km <= 30:
    vv = int(km + 50)
    print(vv if len(str(vv)) == 2 else "0" + str(vv))
elif 35 <= km <= 70:
    vv = int((km - 30) / 5 + 80)
    print(vv if len(str(vv)) == 2 else "0" + str(vv))
elif km > 70:
    vv = 89
    print(vv)
