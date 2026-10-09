#Q1 Import the csv module and read employees.csv using csv.reader().

import csv

with open("employee.csv",'r') as file:
    reader = csv.reader(file)


#Q2 Print every row.

with open("employee.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#3 Skip the header and print only employee rows.

with open("employee.csv",'r') as file:
    reader = csv.reader(file)
    next(reader)
    print("-----------printing csv file without header----------")
    for row in reader:
        print(row)

#4 Print only employee names.

with open("employee.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])

#5. Print employees whose salary is greater than 40000.

with open("employee.csv",'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[3]) > 40000:
            print(row)


#6. Print only employees from the Data Engineering department.

with open("employee.csv",'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[2] == 'Data Engineering':
            print(row)

#7. Calculate the total salary of all employees.

total_sum = 0

with open("employee.csv",'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total_sum = total_sum + int(row[3])
    print(f"the total salary is : {total_sum}")


#8Find the employee with the highest salary.

high_sal = 0

with open('employee.csv','r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:

        current_sal = int(row[3])

        if current_sal > high_sal:
            high_sal = current_sal

    print(f'the highest salary is {high_sal}')


#Q9 Read the same CSV using csv.DictReader() and print each employee's name and salary.

with open('employee.csv','r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row['name'],row['salary'])

#10 Using DictReader(), print only employees who:
'''department = Data Engineering
AND
salary > 40000'''

with open('employee.csv','r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row['department'] == 'Data Engineering' and int(row['salary']) > 40000:
            print(row['name'], "-", row['salary'])


#11 Create students.csv using csv.writer()
'''
id,name,course
1,Manish,Python
2,Rahul,SQL
3,Amit,Spark
'''

with open("students.csv",'w',newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["id","name","course"])
    writer.writerow([1,"Manish",'Python'])
    writer.writerow([2,'Rahul','SQL'])
    writer.writerow([3,'Amit',"Spark"])

'''#12 Use writerow() for one employee
Question: Write the header and one employee.

with open("students.csv","w") as file:
writer = csv.writer(file)

writer.writerow(["id","name","course"])
writer.writerow([4,"Manisha","data specialist"])
'''


'''
Use writerows() for multiple employees
Question: Write 5 employees using writerows().
'''

employees=[
    [101, "Manish", 35000],
    [102, "Rahul", 40000],
    [103, "Amit", 45000],
    [104, "Priya", 38000],
    [105, "Neha", 55000]
]

with open('employees.csv','w',newline="") as file:
    writer = csv.writer(file)

    writer.writerow(['id','name','salary'])
    writer.writerows(employees)

'''
Write employee dictionaries
Question: Create 3 employee dictionaries and write them using DictWriter().
'''

employeess = [
    {'id':101,'name':"manish",'salary':43234},
    {'id':102,'name':"anish",'salary':12345},
    {'id':103,'name':"manishaa",'salary':445734},
    {'id':104,'name':"nish",'salary':42344}
]

with open("employeess.csv","w",newline="") as file:
    fieldname = ["id",'name',"salary"]

    writer = csv.DictWriter(file,fieldnames=fieldname)

    writer.writeheader()
    writer.writerows(employeess)