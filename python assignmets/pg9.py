# s = "inklo"
# x = s.index("l")
# print(x)
# Write a Python program to remove the nth index character from a nonempty string.
# s=input("enter a string : ")
# n=int(input("enter the index : "))
# s1=s[:n]+s[n+1:]
# print(s1)
# Write a Python program that accepts a comma separated sequence of words as input 
# and prints the unique words in sorted form (alphanumerically). 
s=input("enter a comma separated sequence of words : ")
list=s.split(",")
set1=set(list)
list1=list(set1)
list1.sort()
print(",".join(list1))
# Traceback (most recent call last):
#   File "c:\Users\krithika KJ\assignments\python assignmets\pg9.py", line 14, in <module>
#     list1=list(set1)
# TypeError: 'list' object is not callable
