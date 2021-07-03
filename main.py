
#Using if
num = int(input("enter the number?"))
if num%2 == 0:
    print("Number is even")

#using ifelse

age = int (input("Enter your age? "))
if age>=18:
    print("You are eligible to vote !!");
else:
    print("Sorry! you have to wait !!");

#using for loop

list = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in list:
    c = n*i
    print(c)

#while loop
i = 0
str1 = 'javatpoint'

while i < len(str1):
    if str1[i] == 'a' or str1[i] == 't':
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1

#Using String
str1 = 'Hello Python'
print(str1)

str2 = "Hello Python"
print(str2)


str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''
print(str3)

#List
emp = ["John", 102, "USA"]
Dep1 = ["CS",10]
Dep2 = ["IT",11]
HOD_CS = [10,"Mr. Holding"]
HOD_IT = [11, "Mr. Bewon"]
print("printing employee data...")
print("Name : %s, ID: %d, Country: %s"%(emp[0],emp[1],emp[2]))
print("printing departments...")
print("Department 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s, ID: %s"%(Dep1[0],Dep2[1],Dep2[0],Dep2[1]))
print("HOD Details ....")
print("CS HOD Name: %s, Id: %d"%(HOD_CS[1],HOD_CS[0]))
print("IT HOD Name: %s, Id: %d"%(HOD_IT[1],HOD_IT[0]))
print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))

#Tuples
T1 = (101, "Peter", 22)
T2 = ("Apple", "Banana", "Orange")
T3 = 10, 20, 30, 40, 50

print(type(T1))
print(type(T2))
print(type(T3))

#set
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(Days)
print(type(Days))
print("looping through the set elements ... ")
for i in Days:
    print(i)

#dictonary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)

#function
def sum():
    a = 10
    b = 20
    c = a+b
    return c
print("The sum is:",sum())