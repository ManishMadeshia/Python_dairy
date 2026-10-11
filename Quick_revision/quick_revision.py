'''quick reviision'''

'''list'''
'''
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])

#Change 30 to 35.

idx = numbers.index(30)
numbers[idx] = 35

print(numbers)

#Add 60 to the end and 5 to the beginning.

numbers.insert(0,60)
numbers.append(5)
print(numbers)

#remove 35 from a list

numbers.remove(35)
print(numbers)

#predict the output

nums = [10, 20, 20, 30, 20]
print(nums.count(20)) # count = 3
print(nums.index(30))# at index 3

#Reverse [1, 2, 3, 4, 5] without creating a new list.

num = [1,2,3,4,5]
num.reverse()
print(num)

#Create a new list containing only even numbers from 
li = [1, 2, 3, 4, 5, 6]

new_li = []

for i in li:
    if i%2 ==0:
        new_li.append(i)
print(new_li)

#Find both values in 
li = [45, 12, 89, 23, 7]

print(max(li))
print(min(li))

maxx = li[0]
minn = li[0]

for i in li:
    if i > maxx:
        maxx = i
print(maxx)

for i in li:
    if i < minn:
        minn = i

print(minn)

#Remove duplicates from [1, 2, 2, 3, 3, 4, 5, 5] while preserving the original order.

li = [1, 2, 2, 3, 3, 4, 5, 5]
print(set(li))

uni_num = []

for num in li:
    if num not in uni_num:
        uni_num.append(num)
print(uni_num)

'''
'''

#-----------------------tuple-----------------------

data = (10, 20, 30, 40, 50)

print(data[2]) #30
print(data[-1]) #50

#Print (20, 30, 40) using slicing.

idx = data.index(20)
print(data[idx])

idx = data.index(30)
print(data[idx])

idx = data.index(40)
print(data[idx])

#count value
nums = (10, 20, 20, 30, 20)
print(nums.count(20)) #3

#index of 40

data = (10, 20, 30, 40, 50)

idx = data.index(40)
print(data[idx])

#immutability
#data[0] = 100
#print(data) #throw error reason tuple object does not support immutablity


#Create a tuple containing only 10. Why does (10) differ from (10,)?

tu = (10)
print(type(tu))
tu = (10,)
print(type(tu))

#tuple unpacking

student = ("Manish", 25, "Python")

name,age,skill = student
print(name)
print(age)
print(skill)

#Convert [10, 20, 30] into a tuple.

li = [10,20,30]
tuple_li = tuple(li)
print(tuple_li)

#Convert (10, 20, 30) into a list and change 20 to 25.

li_list = list(tuple_li)
print(li_list)

idx = li_list.index(20)
li_list(idx) = 25
print(li_list)
print(type(li_list))



#challenge

employees = (("Manish", 35000),("Rahul", 45000),("Amit", 55000))


for i in range(len(employees)):
    if employees[i][1] > 40000:
        print(employees[i])

#alternative

for name, salary in employees:
    if salary> 40000:
        print(employees[i])


#-----------------------set-----------------------

#predict output
nums = {1, 2, 2, 3, 3, 4}
print(len(nums)) #5

#Add 50 to numbers.

#nums.add(50)

#remove the elemnt
#nums.remove(50)

Q4. remove() vs discard()
What happens when you try to remove 100, which isn't in the set, using each method?

#using remove if element not presnt then it will throw error
#but using discard if element not present then it will handle the error and print none

#nums.remove(100)
nums.discard(100)

#find union 
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

#intersection
print(a.intersection(b))

#difference
print(a.difference(b))

#remove duplicate
s = [1, 2, 2, 3, 4, 4, 5] 
new_s = set(s)
print(s)

#Check whether 30 exists in {10, 20, 30, 40}.
s = {10, 20, 30, 40}

if 30 in s:
    print("yes present")
else:
    print("Not present")

#common skill
manish = {"Python", "SQL", "Spark", "AWS"}
rahul = {"Python", "Java", "SQL", "Docker"}

print(manish.intersection(rahul))

'''

#-------------------dictionary-------------------
'''
employee = {
    "name": "Manish",
    "salary": 35000,
    "department": "Data Engineering"
}

#Print the employee's name.

print(employee["name"])
print(employee["department"])
print(employee["salary"])

#Change the salary to 40000.

employee['salary'] = 40000

#Add "city": "Mumbai".
employee['city'] = 'Mumbai'

#Remove the department using pop().
#employee.pop(['Department'])

print(employee.keys())
print(employee.values())

#print every key and value
student = {"name": "Amit", "age": 22, "course": "Python"}

for key,value in student.items():
    print(key)
    print(value)

#Print the "experience" value if it exists; otherwise return 0, without causing a KeyError

experience = student.get("experience",0)
print(experience)

#Count how many times each character appears in "banana".

text = "banana"
char_counts = {}

for char in text:
    # If char is already in the dictionary, add 1. Otherwise, start at 0 and add 1.
    char_counts[char] = char_counts.get(char, 0) + 1

print(char_counts)


#Create a new dictionary containing employees earning more than 40000.
employees = {
    "Manish": 35000,
    "Rahul": 45000,
    "Amit": 55000,
    "Neha": 30000
}

new_emp = {}

for name,salary in employees.items():
    if salary > 40000:
        new_emp.update({name:salary})
print(new_emp)


#Print each employee's name and salary. Then print only those employees earning above 40000.


company = {
    "emp1": {"name": "Manish", "salary": 35000},
    "emp2": {"name": "Rahul", "salary": 45000},
    "emp3": {"name": "Amit", "salary": 55000}
}

for empid, details in company.items():
    print(f'the employeeid : {empid} ,the employeeDetails : {details}')


for emp in company.items():
    if emp['salary'] > 40000:
        print(emp['name'],emp['salary'])

        '''

'''
#-------------------function----------------
#Write greet() that prints "Hello Manish".
def greet(name='Suresh'):
    print(f"Hello {name}")

greet("manish")
greet()


#Write square(n) that returns the square of a number.

def square(n):
    return n*n

print(square(54))

#Write add(a, b) that returns their sum.

def addd(a,b):
    return a+b

print(addd(3,4))

#Q4. Predict the output

def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(5, 3))

#Write check_even(n) that returns True if even, otherwise False.

def check_even(n):
    if n%2==0:
        return True
    else :
        return False

print(check_even(4))

#Write a function that accepts any number of arguments and returns their sum.

def total(*number):
    return sum(number)

print(total(4,5,6,7,8))

# **kwargs — Accept keyword arguments

def details(**details):
    for key,value in details.items():
        print(key,value)

details(name="manish",city = 'mumbai')


'''

#Use map() and lambda to get [1, 4, 9, 16, 25, 36].
 
li = [1,4,9,16,25,36]

squ_li = list(map(lambda x:x*x, li))

print(squ_li)

#Use filter() to get [2, 4, 6].

li = [1,2,3,4,5,6,8,9,20]

new_li = list(filter(lambda x:x%2==0, li))
print(new_li)

#Return only odd numbers using filter().
new_li = list(filter(lambda x:x%2==1, li))
print(new_li)


#Q4. Convert strings to integers
values = ["10", "20", "30", "40"]

new_values = list(map(lambda x: int(x),values))

print(new_values)

#Q5. Convert names to uppercase

names = ["manish", "rahul", "amit"]

new_names = list(map(lambda name:name.upper(),names))
print(new_names)

#filter salary 
salaries = [25000, 45000, 60000, 35000, 80000]

filter_salary = list(filter(lambda salary : salary> 40000,salaries))

print(filter_salary)

#square every number in list than filter number which is even

nums = [1,2,3,4,5,6]

result = list(map(lambda num : num*2, filter(lambda x : x%2 ==0, nums)))

print(result)

#Q8. Filter names by length

names = ["Raj", "Manish", "Amit", "Priyanka"]
new_names = list(filter(lambda name : len(name) > 4, names))

print(new_names)

#apply discount

prices = [100, 200, 500, 1000]

new_price = list(map(lambda x : x*0.90, prices))

print(f'The New Price After Discount: {new_price}')

#Use filter() to select employees earning above 40000, then use map() to extract only their names.

employees = [
    {"name": "Manish", "salary": 35000},
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 55000},
    {"name": "Neha", "salary": 30000}
]

result = list(map(lambda emp: emp['name'], filter(lambda emp: emp["salary"] > 40000, employees)))

print(result)