K, A, B = map(int, input().split())
bis = 1
money = 0
for i in range(K):
    bis += 1
    print(bis, money)
    if bis >= A:
        money += bis // A
        bis = bis % A
    bis += money * B
print(bis)
