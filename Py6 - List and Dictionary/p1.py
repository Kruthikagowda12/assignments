# 1. Write a Python script to sort (ascending and descending) a dictionary by value. 
s1={'a':"1",'b':"4",'c':"5",'d':"2"}
sorted_asc = sorted(s1.items(), key=lambda x: x[1])
sorted_desc = sorted(s1.items(), key=lambda x: x[1], reverse=True)
print(sorted_asc)
print(sorted_desc)