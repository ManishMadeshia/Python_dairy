#Q1. Create hello.txt and write "Hello Python".
'''
file = open("hello.txt",'x')
content = file.write("Hello Python")


# reading the hello txt file 
file = open('hello.txt','r')
con = file.read()
print(con)
'''

#Q2. Write these three lines into employees.txt:

file = open('employees.txt','a')
employees = ["Manish\n", "Rahul\n", "Amit\n"]

con = file.writelines(employees)

#Q3. Create employee.txt using variables:

file = open('employee.txt','a')
name = "Manish"
age = 25
salary = 35000

file.write(f"{name}\n")
file.write(f"{str(age)}\n")
file.write(f"{str(salary)}\n")

#Q4. Write a number 50000 into a file. Handle the fact that write() requires a string.

file = open('employee.txt','a')
file.write(f"50000")


#5. 

#6. Q6. Use writelines() to write:

skill = ["Python\n", "SQL\n", "Spark\n", "AWS\n"]

file = open("skill.txt",'a')
file.writelines(skill)

file = open("skill.txt",'r')
con = file.read()
print(con)

#7. Q7. What happens if you use writelines() with:
skill = ["Python", "SQL", "Spark"]

file = open("skill.txt",'a')
file.writelines(skill)

file = open("skill.txt",'r')
con = file.read()
print(con)

#Q8. Explain the difference between write() and writelines().
# while write() is use to write a single line
# while writelines() is use to write a multiple line precaution while writing you should use \n otherwise all the string attach

#9. Q9. Create student.txt using variables:

name = "Manish"
course = "Data Engineering"
duration = "6 Months"

file = open("student.txt",'a')
file.write(f"name: {name}\n")
file.write(f"course: {course}\n")
file.write(f"duration: {duration}\n")

file = open("student.txt",'r')
con = file.read()
print(con)


#Q10 — Final practice: Create company.txt and write 5 employee records using a loop. Each employee should have a name and salary.

employees_record = {
    'emp1':{"name":"manish","salary":43253},
    'emp2':{"name":"anish","salary":43343},
    'emp3':{"name":"manish","salary":40000},
    'emp4':{"name":"manish","salary":23000},
    'emp5':{"name":"manish","salary":98372}
}

file = open("companys.txt",'a')

for emp in employees_record :
    name = employees_record[emp]["name"]
    salary =employees_record[emp]["salary"]

    file.write(f"Employees: {emp}\n")
    file.write(f"Name: {name}\n")
    file.write(f"Salary: {salary}\n")
    file.write("\n")