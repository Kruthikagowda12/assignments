# Write a Python program to find the highest 3 values in a dictionary. 
d = {'a': 10, 'b': 45, 'c': 23, 'd': 67, 'e': 34}
values = list(d.values())
values.sort(reverse=True)
print(values[:3])
