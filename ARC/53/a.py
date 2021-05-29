import math
H,W=map(int,input().split())
ans_h = 0
ans_w = 0
if H >= 2:
    ans_h = (H-1)*W
if W >= 2:
    ans_w = (W-1)*H

print(ans_h+ans_w)