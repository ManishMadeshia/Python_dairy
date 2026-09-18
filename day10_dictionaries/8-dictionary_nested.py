#q1. Create a nested dictionary containing two students, with name and age.

students = {
    'student1':{
        'name':"manish",
        'age':25,
        'class':'10th'
    },
    'student2':{
        'name':"bipin",
        'age':23,
        'class':'12th'
    }
}

print(students)

#q2.Create a nested dictionary containing three employees, with name, department, and salary
employees={
    'emp1':{
        'name':"manish",
        'department':"IT",
        'salary':55000
    },
    'emp2':{
        'name':"Bipin",
        'department':"Sales",
        'salary':30000
    },
    'emp3':{
        'name':"Jayesh",
        'department':"Commerce",
        'salary':40000
    }
}

print(employees)

#q3. Print the name of the first student.

print(employees['emp1']['name'])
print(employees['emp1']['department'])
print(employees['emp1']['salary'])

#q4. Print the salary of the second employee.

print(employees['emp2']['salary'])

#q5.Update the age of a student inside a nested dictionary.
students['student1']['age']= students['student1']['age']+1
print(students['student1']['age'])

#q6. Add a city key inside a student's nested dictionary.

students['student1']['city']='Mumbai'
students['student2']['city']='Pune'

print(students)

#q7.Print all student details using nested loops.

for student,details in students.items():
    print(f'{student}:{details}')

#q8. Create a nested dictionary for two products containing name, price, and quantity.

products={
    'product1':{
        'name':"Washing Powder",
        'price':2000,
        'quantity':3
    },
    'product2':{
        'name':"Steel Bottle",
        'price':999,
        'quantity':4
    }
}
print(products)
print(products['product1'])
print(products['product2'])

'''
Perform these operations:

Print Manish's department.
Print Rahul's salary.
Update Manish's salary to 38000.
Add "city": "Mumbai" to Rahul's details.
'''

employees = {
    "emp1": {
        "name": "Manish",
        "department": "Data Engineering",
        "salary": 35000
    },
    "emp2": {
        "name": "Rahul",
        "department": "DevOps",
        "salary": 40000
    }
}

print(employees['emp1']['department'])


search_name = 'Manish'
found = False

for emp_id,emp_details in employees.items():
    if emp_details['name']==search_name:
        print(f'{search_name} works in the {emp_details['department']}')
        found = True
        break

if not found:
    print(f"Employee named '{search_name}' not found.")

print(employees['emp2']['salary'])

employees['emp1']['salary'] = 38000

employees['emp2']['city']="Mumbai"
print(employees['emp2'])


'''
Q10.Create a complete nested dictionary program containing three employees.

Each employee should have:

Name
Age
Department
Salary

Then:

Print all employee details.
Print employees earning more than ₹30,000.
Update one employee's salary.
Add a new key to one employee.
'''

employeess={
    'emp1':{
        'name':"manish",
        "age":24,
        "Department":"IT",
        "Salary":40000
    },
    'emp2':{
            'name':"nisha",
            "age":22,
            "Department":"Sales",
            "Salary":30000
        },
    'emp3':{
            'name':"manisha",
            "age":21,
            "Department":"Account",
            "Salary":20000
        }
}

print(employeess)

for emp, emp_details in employeess.items():
    if emp_details['Salary'] > 30000:
        print(f'-{emp_details['name']}({emp_details['Department']}: {emp_details["Salary"]})')

print(employeess['emp1']['Salary'])

employeess['emp1']['Salary'] = employeess['emp1']['Salary'] + 5000

print(employeess['emp1']['Salary'])

employeess['emp1']['last name'] = "Madeshia"

print(employeess)