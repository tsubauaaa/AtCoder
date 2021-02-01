S = input()
keyboard = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
if keyboard.find(S) in (0, 1, 12, 13, 24, 25):
    print("Do")
elif keyboard.find(S) in (2, 3, 14, 15, 26, 27):
    print("Re")
elif keyboard.find(S) in (4, 16, 28):
    print("Mi")
elif keyboard.find(S) in (5, 6, 17, 18, 29, 30):
    print("Fa")
elif keyboard.find(S) in (7, 8, 19, 20, 31, 32):
    print("So")
elif keyboard.find(S) in (9, 10, 21, 22, 33, 34):
    print("La")
elif keyboard.find(S) in (11, 23, 35):
    print("Si")
