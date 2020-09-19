if __name__ == "__main__":
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        a = i
        b = a+1
        c = a+2
        if a*b+c == N:
            print(f'{a}*{b}+{c}')
            ans += 1

        if a*(b-1)+c == N:
            print(f'{a}*{b-1}+{c}')
            ans += 1
        if a*(b-1)+(c-1) == N:
            print(f'{a}*{b-1}+{c-1}')
            ans += 1
        if a*(b-1)+(c-2) == N:
            print(f'{a}*{b-1}+{c-2}')
            ans += 1

        if a*b+(c-1) == N:
            print(f'{a}*{b}+{c-1}')
            ans += 1
        if a*b+(c-2) == N:
            print(f'{a}*{b}+{c-2}')
            ans += 1
    
    print(ans)
