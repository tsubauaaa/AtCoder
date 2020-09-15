if __name__ == "__main__":
    K = int(input())
    sevens = 0
    ans = -1
    for i in range(K):
        sevens += 7 * 10**i
        if sevens % K == 0:
            ans = i+1
            break
    
    print(ans)

