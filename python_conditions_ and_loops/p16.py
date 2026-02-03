# 5. Take integer inputs from user until he/she presses q ( Ask to press q to quit 
# after every integer input ). Print average and product of all numbers. 
total = 0
count = 0
product = 1
while True:
    num = input("Enter a number (or 'q' to quit): ")
    if num.lower() == 'q':
        break
    try:
        number = int(num)
        total += number
        product *= number
        count += 1
    except ValueError:
        print("Please enter a valid integer or 'q' to quit.")
if count > 0:
    average = total / count
    print("Average:", average)
    print("Product:", product)
else:
    print("No numbers were entered.")