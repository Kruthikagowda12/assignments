# multiply  multiply all the items in a dictionary.:

d = {1: 2, 2: 3, 3: 4, 4: 5}
mul = 1
for value in d.values():
    mul *= value
print(mul)
