N = int(input())
str_N = str(N)

if N <= 10**3-1:
    print(N)
elif 10**3 <= N <= 10**4-1:
    print(str_N[:3]+"0")
elif 10**4 <= N <= 10**5-1:
    print(str_N[:3]+"00")
elif 10**5 <= N <= 10**6-1:
    print(str_N[:3]+"000")
elif 10**6 <= N <= 10**7-1:
    print(str_N[:3]+"0000")
elif 10**7 <= N <= 10**8-1:
    print(str_N[:3]+"00000")
elif 10**8 <= N <= 10**9-1:
    print(str_N[:3]+"000000")
