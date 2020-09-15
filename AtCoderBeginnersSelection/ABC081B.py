if __name__ == "__main__":
    N = int(input())
    ans = 0

    a_list = list(map(int, input().split()))

    while all(a%2==0 for a in a_list):
        a_list = [a/2 for a in a_list]
        ans += 1
    print(ans)