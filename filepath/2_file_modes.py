#1 Open data.txt in read mode.

file = open('employees.csv',"r")
file.close()

#Open data.txt in write mode and write:

file = open('employees.csv','w')
file.write("Hello Python")
file.close()

#append mode

file = open("employees.csv",'a')

file.write("Data Engineering")

file.close

#create a new file

#file  = open("data.txt",'x')
#file.close()

#write three employees

file = open("employees.csv","w")

file.write("Manish\n")
file.write("Manisha\n")
file.write("anish\n")

file.close()

#append priya

file = open("employees.csv",'a')

file.write("Priya\n")

file.close()


# read mode when files doesnt exist

#file = open("abc.txt","r")


#10. Create company.txt and write:
'''Company: ABC Technologies
Department: Data Engineering
Employee: Manish,
Role: Data Engineer
'''

'''
#create a file using x mode
file = open("company.txt",'x')
file.close()

#now writing txt to it
file = open("company.txt","w")
file.write("Company: ABC Technologoies\n")
file.write("Department: Data Engineering\n")
file.write("Employee: Manish\n")

file.close
'''


#now appending txt
file = open("company.txt",'a')
file.write("Role: Data Engineer")
file.close

#to read the stuff

file = open("company.txt",'r')

print(file.read())
file.close()