nums = input()
for i in range(2):
    if i:
        a1 = int(nums[0]) + int(nums[1])
        op1 = "+"
    else:
        a1 = int(nums[0]) - int(nums[1])
        op1 = "-"
    for j in range(2):
        if j:
            a2 = a1 + int(nums[2])
            op2 = "+"
        else:
            a2 = a1 - int(nums[2])
            op2 = "-"
        for k in range(2):
            if k:
                a3 = a2 + int(nums[3])
                op3 = "+"
            else:
                a3 = a2 - int(nums[3])
                op3 = "-"
            if a3 == 7:
                print(f"{nums[0]}{op1}{nums[1]}{op2}{nums[2]}{op3}{nums[3]}=7")
                exit()
