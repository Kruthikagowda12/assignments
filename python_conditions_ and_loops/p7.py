# Write a Python program that counts the number of elements within a list that 
# are greater than 30.
list1 = [10, 25, 35, 45, 55, 65,50]
count = 0
for num in list1:
    if num > 30:
        count += 1
print(count)