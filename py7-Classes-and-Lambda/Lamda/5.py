# Write a Python program to check whether a given string is number or not using Lambda
is_number = lambda s: s.replace('.', '', 1).replace('-', '', 1).isdigit()
text = input("Enter a string: ")
if is_number(text):
    print("It is a number")
else:
    print("It is not a number")
