#  given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
s = int(input("Enter the key to check: "))
if s in d:
    print(f"Key {s}  exists")
else:
    print(f"Key {s} does not exist")
