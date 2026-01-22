# 1. Write a Python program to calculate the length of a string.
s=input("Enter a string: ")
def  func(s):
    count=0
    for i in s:
        count+=1
    return count
print(func(s))


# print(len(s))