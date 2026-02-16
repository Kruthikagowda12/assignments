# Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.  

# Original list: ['red', 'black', 'white', 'green', 'orange']  

# Substring to search: ack Elements of the said list that contain specific substring: ['black'] 
# Substring to search: abc Elements of the said list that contain specific substring: []
strings = ['red', 'black', 'white', 'green', 'orange']
substring = "ack"
filtered_strings = list(filter(lambda s: substring in s, strings))
print(filtered_strings)
