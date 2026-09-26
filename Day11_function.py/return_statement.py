#Create a function add(a, b) that returns the sum.

def fun(a,b):
    return a + b
print(fun(3,2))

#Create square(number) that returns the square.

def squ(a):
    return a*a
print(squ(4))

#Create is_even(number) that returns "Even" or "Odd".

def is_even(number):
    if number%2 ==0:
        return "Even"
    else :
        return "Odd"

print(is_even(3))

#Create find_max(a, b) that returns the larger number.
def find_max(a,b):
    if a>b:
        return "a is greater"
    else :
        return "b is greater"

print(find_max(3,2))

#Create calculate_area(length, width) that returns the area of a rectangle.

def calculate_area(l,w):
    return f"the area of rectangle is : {l*w}"

print(calculate_area(54,32))

'''Q6

Create calculate(a, b) that returns:

addition
subtraction
multiplication
division

Then unpack all four returned values.'''

def calculate(a,b):
    return a+b, a-b, a*b, a/b

addition, substraction, multiplication, division = calculate(3,2)
print(addition)
print(substraction)
print(multiplication)
print(division)

'''Create check_number(number):

If positive → return "Positive"
If negative → return "Negative"
If zero → return "Zero"
'''


def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    elif number == 0:
        return "Zero"
    else:
        return "Something went wrong"

print(check_number(0))
print(check_number(23))
print(check_number(-5))


'''Create calculate_salary(salary, bonus) that returns the total salary.

Then store the returned value in a variable and print it.'''

def calculate_salary(salary,bonus):
    return f"Total Salary is : {salary+bonus}"

print(calculate_salary(34567,8873))

"""9. Create get_employee(name, department, salary) that returns all three values.
unpack them into :
name
department
salary
"""

def get_employee(name,department,salary):
    return name,department,salary


name,department,salary = get_employee(
    "manish",
    "data engineering",
    35000
)

print(name)
print(salary)
print(department)


#q10. return total,avg,max,min

def analyze_number(*number):
    total = sum(number)
    avg = total / len(number)
    maxx = max(number)
    minn = min(number)

    return total,avg,maxx,minn

total,avg,maxx,minn = analyze_number(1,2,3,4,5,6)

print(total)
print(avg)
print(maxx)
print(minn)