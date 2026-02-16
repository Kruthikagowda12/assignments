coords = [(1,-2), (-2,4), (-1,-1), (-8,-3), (0,4), (10,-3)]
min_val = min(min(x, y) for x, y in coords)
shift = -min_val if min_val < 0 else 0
result = [(x + shift, y + shift) for x, y in coords]
print(result)
