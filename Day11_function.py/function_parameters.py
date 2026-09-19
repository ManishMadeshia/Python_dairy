
'''#Parameters are the variables written when defining a function.

eg def greet(name):
    print("Hello", name)

name is parameter

#Argument are the actual value we pass when calling the function

greet("Manish") #manish is an argument

#multiple parameter

def add(a, b):
    return a + b

print(add(10, 20))

a,b is parameter
10,20 is argument

#positional argument
def employee(name,salary):
    print(name,salary)

employee("Manish",34000)

#keyword argument
employee(salary=35000, name="Manish")

#default parameter
def greet(name="Manish"):
    print("Hello", name)

greet()
greet("Rahul")

#multiple defalut parameter
def employee(name, department="IT", city="Mumbai"):
    print(name, department, city)

employee("Manish")

# *args allows a function to accept multiple positional arguments.

eg print(add_all(10, 20, 30, 40))

# **kwargs allows multiple keyword arguments.

'''

#Create a function greet(name) that prints:

def greet(name):
    print(f"hello {name}")

greet("Manish")

#Create a function add(a, b) that returns the sum.

def add(a,b):
    return a+b

print(add(3,4))

#Create a function employee(name, salary).

def employee(name="Manish",salary=33443):
    print(name,salary)

employee("anish",33333)
employee()

#create a function : def greet(name="Manish"):
#Call it once without an argument and once with "Rahul".

def greet(name="Manish"):
    print(f'hello {name}')

greet()
greet("rahul")

#create def calculate_salary(salary, bonus=5000): return total salary

def calculate_salary(salary,bonus):
    return salary+ bonus

print(calculate_salary(30000,3242))

#Create a function multiply(a, b, c) that returns the multiplication of all three numbers.

def mult(a,b,c):
    return a *b *c

print(mult(3,4,5))

#Create a function: def add_all(*numbers): Return the sum of all numbers.

def add_all(*number):
    return sum(number)

result = add_all(10,203,2,3,4,22,11)
print(result)

#create dunction def find_max(*numbers): find large number

def find_max(*number):
    return max(number)

print(find_max(3,4,5,6,7,4))

