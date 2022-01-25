day = input()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

index = days.index(day)

if index != 6:
    print(days.index("Saturday") - index)
else:
    print(0)
