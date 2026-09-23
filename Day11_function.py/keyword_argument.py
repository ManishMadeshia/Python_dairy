#q1.def employee(name, salary):

def employee(name,salary):
    print(f'{name},{salary}')

employee(salary=35000, name="Manish")


#q2. def student(name, age, course):
#Call it using keyword arguments in a different order.

def student(name,age,course):
    print(f"{name}{age}{course}")

student(name="manish",course='IT',age=33)


#q3. def rectangle(length, width): Call it using keywords.

def rectangle(length,width):
    return length*width

print(rectangle(width=33,length=21))


#q4. def employee(name, department, salary): Call it with all three keyword arguments in reverse order.

def employee(name,department,salary):
    print(f'{name},{department},{salary}')

employee(salary=3333,name="anish",department="IT")


#q5. def product(name, price, quantity):Call it using keyword arguments in a random order.

def product(name, price,quantity):
    print(f"{name} {price},{quantity}")

product(quantity=33, price=399,name="MOBILE CASE")


