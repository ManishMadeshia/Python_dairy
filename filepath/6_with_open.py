#1. Read data.txt using with open().
with open("data.txt",'r') as file:
    content = file.read()
    print(content)

#2. Write "Hello Python" to hello.txt using with open().
with open("hello.txt",'a') as file:
    file.write("Hello Python\n")

#3. Append "Data Engineering" to hello.txt.

with open("hello.txt",'a') as file:
    file.write("Data Engineering\n")

#4. Read employees.txt using readlines() and print the list.
with open("employees.txt",'r') as file:
    cont = file.readlines()
    print(cont)

#5. Read employees.txt and print each employee using a for loop.

#1 approach
'''
with open("employees.txt",'r') as file:
    employees = file.readlines()
    for employee in employees:
        print(employee.strip())
'''
#2 approach
with open("employees.txt",'r') as file:
    for employees in file:
        print(employees.strip())

#6Write these three lines using with open():
"""
python
sql
pyspark
"""

with open("plain.txt",'a') as file:
    file.write("Python\n")
    file.write("SQL\n")
    file.write("PySpark\n")

with open("plain.txt",'r') as file:
    con = file.read()
    print(con)

#7. Use with open() and read() to read a file twice. Use seek(0) between the reads.

with open("plain.txt",'r') as file:
    print(file.read())
    print("reading second time: ")
    file.seek(0)
    print(file.read())

#8 Why don't we need file.close() when using with open()?
# it automatically handle

#9. Convert this code to with open():

'''

code : 


file = open("data.txt", "r")
data = file.read()
print(data)
file.close()
'''

#solution 
"""
with open("data.txt",'r') as file:
    data = file.read()
    print(data)

"""

#10. Create employees.txt and write 5 employees with their salaries using with open() and a loop.

emp = {
    "Manish": 35000,
    "bipin": 30000,
    "brijesh":70000,
    'Rohit': 34554,
    "aman":33333
}
with open('empl.txt','a') as file:
    for name,salary in emp.items():
        file.write(f"Name:{name}, Salary: {salary}\n")