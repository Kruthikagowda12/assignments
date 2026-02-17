total=0
count=0
while True:
    num=int(input("enter a number (0 to finish): "))
    if num==0:
        break
    total+=num
    count+=1
if count>0:
    average=total/count
    print("Sum:", total)
    print("Average:", average)

else:
    print("No numbers were entered.")


# d=int(input("Enter 1st number: "))
# d1=int(input("Enter 2nd number: "))
# avg=(d+d1)/2
# sum=d+d1
# print(sum)
# print(avg)
