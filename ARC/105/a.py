import sys

A, B, C, D = map(int, input().split())
target = (A + B + C + D) / 2
if not target.is_integer():
    print("No")
    sys.exit()

if (
    A == target
    or B == target
    or C == target
    or D == target
    or A + B == target
    or A + C == target
    or A + D == target
    or B + C == target
    or B + D == target
    or C + D == target
    or A + B + C == target
    or B + C + D == target
):
    print("Yes")
else:
    print("No")
