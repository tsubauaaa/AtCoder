X = int(input())
five_hand = X // 500
remain = X - 500 * five_hand
five = remain // 5
print(1000 * five_hand + 5 * five)
