#Create a dictionary of three fruits and loop through its keys.

fruits = {
    'mango':1,
    "banana":3,
    'chikoo':4
}

for key in fruits.keys():
    print(f'the key are : {key}')

#Create a student dictionary and print all values using a loop.
student ={
    'name':"manish",
    'age':25,
    'city':"mumbai"
}

for value in student.values():
    print(value)

#Print all key-value pairs using items().

for key,value in student.items():
    print(f'the key is: {key}, the value is: {value}')


#Create an employee dictionary and print only the keys.

employee_record = {
    "emp_id": "EMP101",
    "name": "Arjun Mehta",
    "department": "IT",
    "role": "Cloud Engineer",
    "salary": 95000,
    "is_active": True
}

for key in employee_record.keys():
    print(key)

#Print only the values that are numbers.
for value in employee_record.values():
    if type(value) == int:
        print(value)


#Create a dictionary of marks and print subjects with marks greater than 50.

student_marks={
    'math':85,
    "history":45,
    'geography':88,
    'english':77
}

for subject, marks in student_marks.items():
    if marks > 50:
        print(f"- {subject}: {marks}")


#Count the number of items using a for loop.
count = 0

for key in student_marks.keys():
    count = count +1 
print(count)

#Calculate the sum of all numeric values in a dictionary using a loop.

sum = 0

for value in student_marks.values():
    if type(value) == int:
        sum = sum + value

print(sum)

''' Q8 Print:

All keys
All values
All key-value pairs
Only numeric values
Sum of numeric values'''

employee = {
    "name": "Manish",
    "age": 25,
    "salary": 35000,
    "experience": 2
}

for keys in employee.keys():
    print(keys)

for values in employee.values():
    print(values)

for key,value in employee.items():
    print(f"{key}: {value}")

for values in employee.values():
    if type(values) ==int:
        print(values)

sum_num_value = 0

for values in employee.values():
    if type(values) ==int:
        sum_num_value = sum_num_value + values

print(sum_num_value)


'''
Create a complete program that:

Creates a dictionary of five employees and their salaries.
Prints each employee and salary.
Prints employees earning more than ₹30,000.
Calculates the total salary.
Counts the number of employees.
'''
#Creates a dictionary of five employees and their salaries.

employee_detail ={
    "manish":88888,
    "bipin":99999,
    "suresh":44444,
    "mohan":999999,
    "digvijay":33333
}

print(employee_detail)

#Prints each employee and salary.

for key,values in employee_detail.items():
    print(f'{key}:{values}')

#Prints employees earning more than ₹50,000.
print("employee earning salary > 50000: ")
for employee,salary in employee_detail.items():
    if salary > 50000:
        print(f"{employee}:{salary}")

#Calculates the total salary.

total_salary = 0

for employee,salary in employee_detail.items():
    total_salary = total_salary+salary

print(total_salary)


#Counts the number of employees.

count = 0

for key in employee_detail.keys():
    count = count + 1

print(count)