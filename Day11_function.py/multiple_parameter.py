#q1.Create add(a, b) that returns the sum.

def add(a,b):
    return a+b

print(add(4,3))

#q2. Create subtract(a, b) that returns the difference.

def sub(a,b):
    return a-b
print(sub(4,2))

#q3. Create multiply(a, b, c) that returns the multiplication.
 
def multiply(a,b,c):
    return a*b*c

print(multiply(3,4,6))

#q4.Create student(name, age, course) and print all three values.

def student(name,age,course):
    return f"Student name is :{name},his age is : {age}, course he enrolled: {course}"

print(student("Manish",24,"Data Engineering"))

#q5.Create employee(name, department, salary) and print all details.

def employee(name,department,salary):
    return f'name:{name}, Department:{department}, Salary:{salary}'

print(employee("Manish","Data Engineer", 35000))

