if __name__ == "__main__":
    N = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    alice = []
    bob = []
    i = 0
    for a in a_list:
        if i % 2 == 0:
            alice.append(a)
        else:
            bob.append(a)
        i += 1

    print(sum(alice) - sum(bob))

    
