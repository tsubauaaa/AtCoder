W, H, x, y = map(int, input().split())
area_split_vertical1 = x * H
area_split_vertical2 = (W - x) * H
min_area_split_vertical = min(area_split_vertical1, area_split_vertical2)


area_split_horizon1 = W * y
area_split_horizon2 = W * (H - y)
min_area_split_horizon = min(area_split_horizon1, area_split_horizon2)

min_area = max(min_area_split_vertical, min_area_split_horizon)

print(area_split_vertical1, area_split_vertical2)
print(area_split_horizon1, area_split_horizon2)

area_verticals = [area_split_vertical1, area_split_vertical2]
area_horizons = [area_split_horizon1, area_split_horizon2]

if min_area == area_split_vertical1 or min_area == area_split_vertical2:
    if min_area == area_split_horizon1 or min_area == area_split_horizon2:
        ans = 1
    else:
        ans = 0
elif min_area == area_split_horizon1 or min_area == area_split_horizon2:
    if min_area == area_split_vertical1 or min_area == area_split_vertical2:
        ans = 1
    else:
        ans = 0

print(min_area, ans)
