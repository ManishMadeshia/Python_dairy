#Check Apple exists.
fruits = ['mango','banana','chikoo','watermelon','apple']

if 'apple' in fruits:
    print("apple exists in fruits list")
else:
    print("dont exist")

#Check Mango exists.
if 'mango' in fruits:
    print("mango exist")
else:
    print("not exists")

#Check Mumbai exists.
cities = ['mumbai','pune','bangalore']

if 'mumbai' in cities:
    print("Mumbai exists")

#Find index of Banana.
if 'banana' in fruits:
    print(fruits.index('banana'))

#find index of pune
if 'pune' in cities:
    print(cities.index('pune'))

#Count occurrence of 10.

c = [1,2,3,4,5,10,10,11]
print(c.count(10))

#count occurence of mango
print(fruits.count('mango'))

#Check employee exists.

emp = ['manish','anish','bipin','gopal']

emp_name = input("Enter name to check: ")
if emp_name in emp:
    print(f'{emp_name} empname exists' )
else:
    print("not exists")