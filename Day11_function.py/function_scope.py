#Create a local variable name inside a function and print it.
def fun(name):
    print(name)
fun("manish")


#Try to access a local variable outside the function. Observe the error.

def fun(name):
    print(name)  #local scope
fun("manish")

#print(name)   #accessing local scope outside function

#Create a global variable name and access it inside a function.

name = "manish"

def fun1():
    print(name)

fun1()

#Create a global variable age = 25 and create a local age = 30 inside a function. Print both.

age = 25

def ages():
    age = 30
    print(age)

ages()

#Create a global variable salary = 35000. Print it from inside a function.

salary = 35000

def sal():
    print(salary)

sal()

#Create a function that tries to change count to 20 without using global. Observe what happens.
count = 10

def countt():
    count = 20
    print(count)

countt() #it print 20 beacuse pyhton create a new varibale of count 20 reason we didnt tell expcility to update global count = 20

#Then print count outside the function.

count = 10

def countt():
    global count
    count = 20
    print(count)

countt()


#Create a global variable: company = "ABC", Create a function that creates a local variable with the same name:

company = 'ABC'

def comp(company):
    print(company)

comp("ABC")

#Create a function that has a local variable total and returns it. Print the returned value outside the function.

def var(total):
    return total

print(var(33))

'''Create:

salary = 35000

Create a function employee() that:

Creates local variable bonus = 5000
Accesses the global salary
Calculates total salary
Returns the total
Prints the returned total outside the function'''

salary = 44444
def employee():
    bonus = 5000
    global salary
    total = salary + bonus
    return total

print(employee())