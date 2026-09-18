#Create a dictionary of fruits and remove "banana" using pop().
fruits = {
    "apple":5,
    "mango":3,
    "banana":6
}
print(fruits)
print(type(fruits))
fruits.pop('banana')
print(fruits)

#Create a student dictionary and remove "age" using del.
student={
    'name':"Manish",
    'age':25,
    'Class':"10th"
}

print(student)
del student['age']

#Create an employee dictionary and remove the last inserted item using popitem().
employee={
    'name':"Manish",
    'age':25,
    'class':"btech"
}

last_pop_item = employee.popitem()
print(last_pop_item)

#Print the removed key-value pair from popitem().
employee={
    'name':"Manish",
    'age':25,
    'class':"btech"
}

last_pop_item = employee.popitem()
print(last_pop_item)

#Create a dictionary and remove all items using clear().
student = {
    "name": "Manish",
    "age": 25
}

student.clear()

print(student)

#Try removing a non-existing key using pop() and observe the error.
#employee.pop("job") #if not present it will throw error 

#Use pop() with a default value to avoid an error.
employee.pop("job",None)


#Create a dictionary with five key-value pairs and remove two specific keys.

dic = {
    'name':"Manish",
    'age':24,
    'job':"data engineer intern",
    'salary':25000,
    'city':"mumbai"
}

print(dic)

rem_dic = dic.pop('city')
print(rem_dic)


'''Perform these operations:

Remove "age" using pop().
Remove "salary" using del.
Remove the last inserted item using popitem().
Print the final dictionary. '''

employee = {
    "name": "Manish",
    "age": 25,
    "department": "Data Engineering",
    "salary": 35000
}

pop_item = employee.pop('age')
del employee['salary']
last_pop_item = employee.popitem()
print(employee)

'''
Create a complete program that:

Creates a dictionary.
Adds a new key.
Updates an existing value.
Removes one key using pop().
Removes one key using del.
Prints the final dictionary.
'''

dictt={
    'name':'Manish',
    'city':'Mumbai'
}

#add new key
dictt['age']=24
print(dictt)

#update
dictt['age'] = 25

#remove usign pop
remove_pop = dictt.pop('age')

#remove using del
del dictt['city']

print(dictt)