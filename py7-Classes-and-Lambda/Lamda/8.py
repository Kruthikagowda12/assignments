# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string
string = "PaceWisd0m"
is_valid = lambda s: all([
    len(s) >= 10,
    any(c.isupper() for c in s),
    any(c.islower() for c in s),
    any(c.isdigit() for c in s)
])
print("valid string" if is_valid(string) else "invalid string")