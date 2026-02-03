# A student will not be allowed to sit in exam if his/her attendence is less than 
# 75%. 
# Take following input from user 
# Number of classes held 
# Number of classes attended. 
# And print 
# percentage of class attended 
# Is student is allowed to sit in exam or not. 
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
attendance = (classes_attended / classes_held) * 100
print("Attendance percentage:", attendance)
if attendance< 75:
    print("Student is not allowed ")
else:
    print("Student is allowed")

