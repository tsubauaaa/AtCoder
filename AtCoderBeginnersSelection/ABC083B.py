if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = []
    for n in range(1, N+1):
        str_n_list = [int(s) for s in str(n)]
        if A <= sum(str_n_list) <= B:
            ans.append(n)

    print(sum(ans))

