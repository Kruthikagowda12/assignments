# You are given with a list of integer elements. Make a new list which will store 
# square of elements of previous list. 
list1 = [1, 2, 3, 4, 5]
squared_list = []
for num in list1:
    squared_list.append(num ** 2)
print("Squared list:", squared_list)
