# Write a Python program to check a dictionary is empty or not
n = int(input("Enter number of key-value pairs: "))
d = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
if not d:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
print(d)

