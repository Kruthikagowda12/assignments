lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = []
for item in lst:
    if item not in new_list:
        new_list.append(item)
print(new_list)

