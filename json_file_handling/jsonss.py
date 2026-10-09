'''
Q1. Write a Python dictionary to JSON
Question: Create an employee dictionary and save it to employee.json.

import json

employee = {
    'name':'Manish',
    'salary':54322,
    'department':"data engineering"
}

with open('employee.json','w') as file:
    json.dump(employee,file)

'''
#2. Question: Save the employee dictionary in a readable JSON format.

import json

employee = {
    'id': 101,
    'name':"manish",
    'salary':54322,
    'department':"Data Engineering"
}

with open("employee.json",'w') as file:
    json.dump(employee,file,indent=2)


#3. Question: Read employee.json and print the complete dictionary.

with open('employee.json','r') as file:
    employee = json.load(file)

    print(employee)

#Q4. Print specific values: Question: Read the JSON and print:

with open("employee.json",'r') as file:
    employee = json.load(file)

    print(f"Name: {employee['name']}")
    print(f'Salary : {employee['salary']}')

#q5. Create 3 employee dictionaries and save them to employees.json.

employee = [
    {"name": "Manish", "salary": 35000},
    {"name": "Rahul", "salary": 40000},
    {"name": "Amit", "salary": 45000}
]

with open('employee.json','w') as file:
    json.dump(employee,file,indent=4)