'''
#Q1. Write a python program to print 'Hello World"
print("hello world")

#Q2. WRITE A PYTHON PROGAM THAT TAKES A USER INPUT AN DPRINTS IT
A = input("TYPE ANYTHING: ")
print(F'INPUT ENTER BY USER : {A}')

#Q3. WRITE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE , NEGATIVE, ZERO
num = int(input("ENTER A NUMBER : "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("zero number")
else:
    print("Negative number")

#Q4. write a program to find the largest of three number

a= int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

if a > b and a > c :
    print("A is greater ")
elif b > c and b> a:
    print("b is greater")
else :
    print("c is greater")

#Q5. Write a program to find factorial of a number

num = int(input("enter a num: "))

factorial = 1

for i in range(1,num+1):
    factorial = factorial * i

print(factorial)



#Q6. create a varibale of different data type : int, float, string, and boolean . print their value and type

a = 12
b = 23.2
c = 'manish'
d = True
e = False

print(f'their datatype is {type(a)} and value is {a}')
print(f"The datatype is {type(b)} and value is {b}")
print(f"The datatype is {type(c)} and value is {c}")
print(f"The datatype is {type(d)} and value is {d}")
print(f"The datatype is {type(e)} and value is {e}")


#Q7. Write a python program to swap the value of two varibale

a = 3
b = 2
a,b = b,a
print(a,b)

#Q8. write a python program to convert celsius to fahrenheit

c = float(input("Enter a Temperature in C: "))

f = (c * 9/5 ) + 32

print(f'temperature in fahrenheit: {f}')

#Q8. write a python program to convert fahrenheit to celsius

f = float(input("Enter a Temperature in f: " ))

c = (f-32)*5/9
print(c)

#Q9. python program to concatenate two strings

a = 'manish'
b = 'madeshia'

print(a+ " "+b)

str1 = input("enter first string")
str2 = input("Enter second string")

result = str1 +" " + str2

print(result) 

#Q10. write a python program to check if a variable is of specific datatype 

a = 7

if type(a) == int:
    print("integer datatpe")
elif type(a) == float:
    print("float datatype")
elif type(a) == str:
    print("String datatype")
else :
    ("not in list of int, float, string")


'''



#------------------arithmetic operator----------------
#11. write a python program to perform addition,subtraction,multiplication,division.

a = 10
b = 33

print(a+b) #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b) #division
print(a//b) #floor division
print(a%b)  #modulos operator


#12. write a python progem to demonstrate comparsion operator equal to, not equal to , greater than, less than ,

a = 12
b = 33

#greater than
if a>b:
    print("a is greater")
else : 
    print('b is greater')

#equal to 
if a==b :
    print("a &b are equal")
else:
    print("not equal")

# less than operator
if a < b :
    print("a is greater")

#not equal operator
if a != b:
    print("not equal")


#13. write a python program to demonstrate logical operator : and , or , not

age = 21
salary = 20000
is_eliglible = True

if age >= 18 and salary >= 30000:
    print("Eligible for loan")
else:
    print("Not eligible")

#--------or-----------

if age >= 18 or salary >=30000:
    print("Partial eliglible! Need to talk with management")

#-----------not-----

if not is_eliglible :
    print("not eliglible")
else:
    print("Eliglible")

#14. program to calculate the square of a number

num = int(input("Enter a no: "))

squ = num * num
print(f"the square of num is : {squ}")

#15. program to check if a num is odd or even

num = int(input("Enter a num: "))

if num <=0:
    print("please enter num greater than 0")
else:
    if num%2 == 0:
        print("even")
    else:
        print("Odd")

#Q16. program to find sum od first n natural no

n = int(input("enter a no: "))

sum = 0

for i in range(1,n+1):
    sum = sum +i
print(sum)

#Q17.program to check leap year


