s1= input("enter a string : ")
n=s1.find("not")    
p=s1.find("poor")
if p>n and n!=-1 and p!=-1:
    s1=s1.replace(s1[n:p+4],"good") 
    print(s1)
else:
    print(s1)

