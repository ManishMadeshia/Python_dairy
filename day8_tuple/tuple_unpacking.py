#Q1. unpack into name,age,city

person = ("Manish", 25, "Mumbai")
name,age,city = person
print(name,age,city)

#q2. employee = ("Rahul", "Developer", 50000) unpcak into three variable

employee = ("Rahul", "Developer", 50000)
name,job,salary = employee
print(name,job,salary)

#q3. numbers = (10, 20, 30) unpcak into a,b,c

numbers = (10, 20, 30)
a,b,c = numbers
print(a,b,c)

#q4. unpack student = ("Amit", 22, 85)
student = ("Amit", 22, 85)
name , age, marks = student
print(student)

#Q5. Swap two variables using tuple unpacking:
a=10
b=20

a,b = b,a
print(a,b)

#q6. Use unpacking with: Store the first two values in a, b and the remaining values in another variable using *.
numbers = (10, 20, 30, 40, 50)

a,b,*c = numbers
print(a)
print(b)
print(c)

#q7. Use unpacking to store the first fruit separately and all remaining fruits in another variable.

fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")
a,*remain = fruits
print(a)
print(remain)

#q8. name,job,salary,city,experience

employee = ("Manish", "Data Engineer", 60000, "Mumbai", 2)

name,job,salary,city,experience = employee
print(name)
print(job)
print(salary)
print(city)
print(experience)

#q10. Use unpacking to store: first value in first, last value in last,all middle values in middle

data = (10, 20, 30, 40, 50, 60)
first , *middle, last = data
print(last)
print(first)
print(middle)