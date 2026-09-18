#Create a dictionary of three fruits and print all keys using keys().

fruits = {
    'mango':1,
    'banana':3,
    'chikoo':4
}

print(fruits)
print(fruits.keys())

#Create a dictionary of student details and print all values using values().
print(fruits.values())

#Print all key-value pairs using items().
print(fruits.items())

#Find the number of items in a dictionary using len().
print(len(fruits))

#Create a copy of a dictionary using copy().
fruits_copy = fruits.copy()
print(f'the copy fruits_copy: {fruits_copy}')

#Create a new dictionary using dict.fromkeys() with these keys:

#Use fromkeys() with a default value of "Not Available".

#Create a dictionary with five key-value pairs and print its keys, values, and items.
employee = {
    "name": "Manish",
    "department": "Data Engineering",
    "salary": 35000,
    "city": "Mumbai",
    'job':"Data Engineer"
}

print(employee.items())
print(employee.values())
print(employee.keys())

'''Print:

All keys
All values
All key-value pairs
Total number of items'''

employee = {
    "name": "Manish",
    "department": "Data Engineering",
    "salary": 35000,
    "city": "Mumbai"
}

print(employee.keys())
print(employee.values())
print(employee.items())
print(len(employee))

'''
Create a complete program that:

Creates a dictionary.
Prints its keys.
Prints its values.
Prints its items.
Creates a copy.
Creates a new dictionary using fromkeys().
'''

new_dic = {
    'name':"manish",
    'age':24,
    'city':"mumbai",
    'location':"Malad west"
}

print(new_dic.keys())
print(new_dic.values())
print(new_dic.items())
copY=new_dic.copy()
print(copY)