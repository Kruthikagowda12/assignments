# A company decided to give bonus of 5% to employee if his/her year of 
# service is more than 5 years. 
# Ask user for their salary and year of service and print the net bonus amount. 
salary = float(input("Enter salary: "))
y_o_s = int(input("Enter your yfs: "))
if y_o_s > 5:
    bonus = salary * 0.05
    print("bonus amount is:", bonus)
else:
    print("No bonus")
