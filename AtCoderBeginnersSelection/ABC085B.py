if __name__ == "__main__":
    N = int(input())
    mochis = []
    for n in range(N):
        mochi = int(input())
        mochis.append(mochi)

    print(len(set(mochis)))