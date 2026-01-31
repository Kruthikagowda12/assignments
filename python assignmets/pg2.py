# 2. Write a Python program to count the number of characters (character frequency) in a string. 
s = input("Enter a string: ")
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)







