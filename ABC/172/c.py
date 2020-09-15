if __name__ == "__main__":
    N, M, K = map(int, input().split())
    input_a = input()
    A = [int(a) for a in input_a.split()]
    input_b = input()
    B = [int(b) for b in input_b.split()]

    read = K
    ans = 0
    books = []

    for i in range(N+M):
        if i % 2 != 0:
            print(i)
            books.append(B[i])
        else:
            books.append(A[i])
    for book in books:
        if read >= book:
            read -= book
            ans += 1
        else:
            break 
    print(ans)
