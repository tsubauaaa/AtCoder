if __name__ == "__main__":
    N = int(input())
    cards = list(map(int, input().split()))
    cards.sort(reverse=True)
    alice = []
    bob = []
    for index, card in enumerate(cards):
        if index%2 == 0:
            alice.append(card)
        else:
            bob.append(card)

    print(sum(alice)-sum(bob))

