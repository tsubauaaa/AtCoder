if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = []

    for i in range(1, N+1):
        if A <= sum(map(int, str(i))) <= B:
            ans.append(i)

    print(sum(ans))