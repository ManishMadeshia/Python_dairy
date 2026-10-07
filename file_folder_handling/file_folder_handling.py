import os

#2. Get Current Working Directory
print(os.getcwd())

#3. Check if a file/folder exists
print(os.path.exists("employee.csv"))

#4. check file
print(os.path.isfile("employee.csv"))

#5. check folder
print(os.path.isdir("data"))

#6. create folder
os.mkdir('Data')  

#if file exist will get error

if not os.path.isdir('data'):
    os.mkdir('Data')

#7. list file and folder

print(os.listdir())

#7. Join Paths

path = os.path.join('data','employees.csv')
print(path)

#remane file 
os.rename('old.txt','new.txt')

