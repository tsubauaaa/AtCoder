SA = input()
SB = input()
SC = input()

cards = {"a": SA, "b": SB, "c": SC}
turn = "a"

while True:
    if cards[turn] == "":
        break
    next = cards[turn][0]
    cards[turn] = cards[turn][1:]
    turn = next

print(turn.capitalize())
