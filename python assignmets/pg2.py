# 2. Write a Python program to count the number of characters (character frequency) in a string. 

# s = input("Enter a string: ")
# def func(s):
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char, 0) + 1
#     return freq
# print(func(s))

def func(s):
  count = 0
  for char in s:
    count += 1
  return count

my_string = "hello"
length = func(my_string)
print(f"The length of the string is: {length}")



