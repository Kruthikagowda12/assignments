lst = []

n = int(input("Enter how many elements: "))

for i in range(n):
    lst.append(input("Enter value: "))

print("List:", lst)

x = input("Enter element to delete: ")

for i in range(len(lst)):
    if lst[i] == x:
        lst.pop(i)
        print("Deleted")
        break
else:
    print("Not found")

print("Updated list:", lst)
