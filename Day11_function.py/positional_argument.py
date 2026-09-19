#q1. create employee

def employee(name,age):
    return f"name:{name}, age:{age}"

print(employee("manish",22))
print(employee(24,"Manish")) # i have change the postion the value store differently as postion matter 

#q2. create student

def student(name,age,course):
    return f'Name :{name}, Age:{age}, Course: {course}'

print(student("Manish",24,"IT ENGINEERING"))

#q3. create rectangle and calculate the area

def rectangle(length,width):
    return length * width

print()