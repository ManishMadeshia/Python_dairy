#create a varibale

file_name = 'data.txt'

print(file_name)

#2. Import os and print the current working directory using:

import os

d = os.getcwd()
print(d)
print(os.getcwd())

#3.Check whether the file exists using os.path.exists().
path = 'data.txt'
print(os.path.exists(path))

#4.Check whether "data.txt" is a file using:

print(os.path.isfile(path))

#5. is directory
print(os.path.isdir(path))

#6
import os

path = "data/employees.csv"
print(os.path.exists(path))


#7 create a absolute path

#Python → data → employees.csv
path = r"C:\Users\Manish\Documents\Python\data\employees.csv"
print(path)


#8 . create a relative path for : data-sales-sales.csv

path = "data\sales\sales.csv"
print(path)

#9. Whether it exists
#Whether it's a file
#Whether it's a directory

import os

path = 'data\employees.csv'
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))

#10. Write a program that prints:

#Path: data/employees.csv
##Exists: True/False
#File: True/False
#Directory: True/False


Path = "data/employees.csv"

print(f"Path: {Path}")
print(f"Exists : {os.path.exists(Path)}")
print(f"File: {os.path.isfile(Path)}")
print(f"Directory: {os.path.isdir(Path)}")