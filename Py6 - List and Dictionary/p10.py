# remove a key from a dictionary.
s1 = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter key to remove: ")
if key in s1:
    del s1[key]
    print("Updated:", s1)
else:
    print("Key not found")

