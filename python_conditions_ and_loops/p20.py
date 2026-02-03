
list1 = [10, "hello", 3.14, 25, "world", 2.71, 42, "python", 1.61]
even_numbers = []
odd_numbers = []
strings = []
for item in list1:
    if isinstance(item, int):
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            odd_numbers.append(item)
    elif isinstance(item, str):
        strings.append(item)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Strings:", strings)
