
#Read the entire data.txt using read().
file = open("data.txt","r")

content = file.read()
print(content)

#Read only the first line using readline().

file = open("data.txt",'r')
content = file.readline()
print(content)

#Read the first two lines using two readline() calls.
file = open("data.txt",'r')

print(file.readline())
print(file.readline())

#Read all lines using readlines().

file = open("data.txt",'r')

content = file.readlines()
print(content)

#Print each line separately from the list returned by readlines().

file = open("data.txt",'r')
contents = file.readlines()
for content in contents:
    print(f"{content}")

#What is the difference between read() and readlines()?

#.......read() read entire value that file content
#..........redlines() read entire value but theee value are going to return in a list with \n

#What happens when you call readline() three times?
#.............totally depend how we are calling eg

#readline() calling three time then it will print the first line , second line, thrird line

#What will the second read() return?

file = open("data.txt",'r')
content = file.readline()
content= file.readline()

#it will not read the file again as the first readline read the entire file and move the file pointer to end so the second read return an empty string beacuse there is nothin left to read.

#Create employees.txt containing:
"""
file = open("employees1.txt",'x')
file.write("Manish\n")
file.write("Rahul\n")
file.write("Amit\n")
file.write("Priya\n")   


file = open("employees1.txt",'r')
content = file.readlines()
print(content)

"""


file = open("employees1.txt",'r')
contents = file.readlines()
for content in contents:
    print(f"Employees: {content.strip()}")


#Q5. use f string to write 
"""
Name: Manish
Role: Data Engineer
Salary: 35000
"""

file = open("employee.txt",'a')
file.write(f"Name: Manish\n, Role: Data Engineer\n,Salary:35000")
file = open("employee.txt",'r')
con = file.read()
print(con)