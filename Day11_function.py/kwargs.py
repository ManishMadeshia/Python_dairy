#q1. Create employee(**details) and print the dictionary.

def employee(**details):
    print(details)

employee(name="manish",age=24)

#q2. Question: Print every key and value using a loop.

def employee(**details):
    for key,value in details.items():
        print(f'{key}:{value}')

employee(name='Manish',age=24,department="IT",Salary=23344)

#q3.Question: Create student(**details) and print all details.

def student(**details):
    for key, value in details.items():
        print(f"{key}:{value}")

student(name="Manish",age=24,year = 'final year', Stream="IT engineering")

#q4. Create product(**details) and print all details.

def product(**details):
    for key,value in details.items():
        print(key,":",value)

product(
    name = 'laptop',
    price = 50000,
    quantity = 4
)

#q5. Print only the "name" value.

def person(**details):
    print(details['name'])

person(
    name="Manish",
    age=25,
    city="Mumbai"
)

#q6. Check whether "salary" exists. If yes, print it.

def employee(**details):
    if 'salary' in details:
        print("salary:",details['salary'])


employee(
    name="Manish",
    salary=35000
)

#q7.Question: Print only details whose values are integers.

def employee(**details):
    for key,value in details.items():
        if type(value) == int:
            print("the int value are: ")
            print(key,":",value)


employee(
    name="Manish",
    age=25,
    salary=35000,
    city="Mumbai"
)

#q8.Question: Calculate the total of numeric values.

def employee(**details):
    total = 0

    for value in details.values():
        if isinstance(value,(int,float)):
            total = total + value

    print("Total:", total)

employee(
    age=25,
    salary=35000,
    bonus=5000
)