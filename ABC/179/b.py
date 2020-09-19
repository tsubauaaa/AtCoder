if __name__ == "__main__":
    N = int(input())
    doublet_count = 0
    is_doublet = False

    for i in range(N):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            doublet_count += 1
        else:
            doublet_count = 0
        if doublet_count == 3:
            is_doublet = True
            break
    
    
    if is_doublet:
        print('Yes')
    else:
        print('No')