#Print all fruits using loop.

fruits = ['mango','banana','chikoo','grapes']
for fruit in fruits:
    print(fruit)

#print all cities using loop
cities = ['mumbai','lucknow','gorakhpur']
for city in cities:
    print(cities)

#Print all marks using loop.
marks = [55,66,77,88,84]
for mark in marks:
    print(marks)

#Print only even numbers.
num = [2,1,2,3,4,3,5,6,45,9]
for n in num:
    if n%2==0:
        print(n)

#Print only odd numbers.
for n in num:
    if n%2==1:
        print(n)

#find sum using loop
sum = 0
for i in num:
    sum = sum+i
print(sum)

#Find maximum using loop.

num = [2,1,2,3,4,3,5,6,45,9]
max = 0
for i in num:
    if i > max:
        max = i
print(max)

#Count elements using loop.

count = 0

for i in num:
    count= count+1
print(count)

#Print squares of numbers.
for i in num:
    print(i*i)

#Print student names one by one.
students = ["Alice", "Bob", "Charlie", "David"]

for name in students:
    print(name)
