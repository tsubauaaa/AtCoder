if __name__ == "__main__":
    S = input()
    x = ['A', 'C', 'G', 'T']
    ans = 0
    now = 0
    for s in S:
        if s in x:
            now += 1
        else:
            now = 0
        ans = max(now, ans)
    print(ans)