#q1. Create a tuple containing 5 cities.
cities = ('mumbai','kolkata','delhi','pune','goa')
print(cities)
print(type(cities))

#q2. Print the first, third and last elements.
print(cities[0])
print(cities[-1])
print(cities[2])

#q3. Find the length of the tuple.
print(len(cities))

#Q4. Check whether "Mumbai" exists using in.
if 'mumbai' in cities:
    print("yes exists")

#q5. Check whether "Delhi" does not exist using not in.
if 'delhi' not in cities:
    print("not exists")
else:
    print("exists")

#q6.Find the total using sum().
numbers = (10, 20, 30, 40, 50)
print(sum(numbers))

#q7.Find the highest and lowest number.
print(min(numbers))
print(max(numbers))

#Q8 Calculate the average.
print(sum(numbers)/len((numbers)))

#q9. Find how many times 10 occurs:

numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))

#q10. Find the index of 30.
idx = numbers.index(30)
print(idx)

#q11. Print the first three elements using slicing.
print(numbers[0:3])

#Q12. Print the last two elements using slicing.
print(numbers[-1:-3:-1])

#q13. Reverse the tuple using slicing.
print(numbers[::-1])

#q14. Print every second element:
print(numbers[0::2])

#q15. Unpack: into three variable
person = ("Manish", 25, "Mumbai")
name,age,city = person
print(name)
print(age)
print(city)

#q16. swap using tuple packing
a = 100
b = 200

num = a,b
print(num)

#Q17. Try to change an element of:
numbers = (10, 20, 30)

#numbers[1] = 20
print(numbers) #tuple are immutable

#q18. Convert this tuple into a list:
numbers = (10, 20, 30, 40)

numberss = list(numbers)
print(numberss)
print(type(numberss))


#q19. After converting to a list, change 30 to 100, then convert it back to a tuple.
idx = numberss.index(30)
numberss[idx] = 100
print(numberss)

#q20. Using a loop, create a tuple containing only numbers greater than 50.
numbers = (10, 25, 40, 55, 70, 85)

filter_list = []

for num in numbers:
    if num > 50:
        filter_list.append(num)

print(filter_list)

#Q21. Using a loop, create a tuple containing the squares:
numbers = (2, 4, 6, 8, 10)
squ = []

for num in numbers:
    squ_value = num**2
    squ.append(squ_value)

print(squ)

#q22. Count the number of passing students using a loop.

marks = (35, 67, 82, 29, 91, 45)

pass_marks = []
fail_marks = []

for mark in marks:
    if mark >= 35:
        pass_marks.append(mark)
    else:
        fail_marks.append(mark)

print(f'the count of passing student: {len(pass_marks)}')
print(f'the count of failing students:{len(fail_marks)}')

#q23. Create a tuple containing only values that aren't None.

data = (10, None, 20, None, 30, 40, None)
new_data = []

for i in data:
    if i is not None:
        new_data.append(i)

print(new_data)


#Q24. Unpack the tuple and print all five values with labels.

employee = ("Manish", "Data Engineer", 60000, "Mumbai", 2)

Name,Job_role,Salary,city,employee_id = employee

print(Name,Job_role,Salary,city,employee_id)

'''q25
Given: numbers = (10, 20, 30, 40, 50, 60, 70, 80)
Using tuple unpacking, separate:

First element → first
Last element → last
Everything in between → middle'''
numbers = (10, 20, 30, 40, 50, 60, 70, 80)

first,*middle,last = numbers
print(first)
print(middle)
print(last)