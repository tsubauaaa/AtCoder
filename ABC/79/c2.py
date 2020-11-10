nums = [s for s in input()]
ops_len = len(nums) - 1
ops = []
for i in range(2 ** ops_len):
    op = []
    for j in range(3):
        if (i >> j) & 1:
            op.append("+")
        else:
            op.append("-")
    ops.append(op)
    for op in ops:
        formula = str(nums[0] + op[0] + nums[1] + op[1] + nums[2] + op[2] + nums[3])
        if eval(formula) == 7:
            print(formula + "=7")
            exit()
