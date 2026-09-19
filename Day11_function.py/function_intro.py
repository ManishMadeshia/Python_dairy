#Create a function greet() that prints "Hello, Manish".

def greet():
    print("Hello Manish")

greet()

#Create a function square(number) that prints the square of a number.

def squ(n):
    print(n*n)

squ(8)

#Create a function add(a, b) that returns the sum.
def num(a,b):
    return a+b

print(num(3,4))

#Create a function subtract(a, b) that returns the difference.

def sub(a,b):
    return a -b 

print(sub(3,4))

#Create a function multiply(a, b) that returns the multiplication.
def mult(a,b):
    return a*b 

print(mult(3,4))

#Create a function is_even(number) that returns "Even" or "Odd".
def is_number(n):
    if n%2==0:
        print("even number")
    else:
        print("Odd NUmber")

is_number(4)

#Create a function find_max(a, b) that returns the larger number.
def find_max(a,b):
    if a>b:
        return a
    else:
        return b
    

print(f"the greater num: {find_max(3,4)}")

#Create a function calculate_salary(salary, bonus) that returns:

def calculate_salary(salary,bonus):
    return salary + bonus

print(calculate_salary(40000,3923))

#Create a function calculate_average(a, b, c) that returns the average of three numbers.

def calculate_average(a,b,c):
    return a+b+c /3

print(calculate_average(3,5,3))

#create function employee_details(name, department, salary)

def employee_details(name,deparment,salary):
    return F'Employee:{name}\nDepartment:{deparment}\nSalary:{salary}'

print(employee_details("manish","IT",30000))