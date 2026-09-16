#creating dictionaries

empty_d = {}
print(type(empty_d))

students = {'name':'manish','age':24,'grade':19}
print(students)

students = {'name':"manish","age":24,"name":"bipin"}
print(students)

#accessing dictinoary element
students = {'name':'manish','age':24,'grade':19}
print(students['name'])

print(students['age'])

### Accessing using get() method

print(students.get('grade'))
print(students.get('name'))
print(students.get("marks",'not available'))

## Modifying Dicitonary Elements
## Dictionary are mutable,so you can add, update or delete elements

students['age'] = 25
print(students)

students['address'] = 'Mira road Mumbai-400101'
print(students)

del students['grade'] ## delete key and value pair

print(students)

## Dictionary methods
keys = students.keys()
print(keys)
value = students.values()
print(value)
item = students.items()
print(item)

#shallow copy and deep copy
#in shallow copy the change occur in one varible 
#but in deep copy the changes occur in both varibale


students_copy = students
print(students)
print(students_copy)
students['name']='manish2'
print(students)
print(students_copy)


#shallow copy
students_copy_1 = students.copy()
print(students_copy_1)
print(students)

students['name'] = 'manish3'
print(students_copy_1)
print(students)

#### Iterating Over Dictionaries

for keys in students.keys():
    print(keys)

for values in students.values():
    print(values)

for items in students.items():
    print(items)

## Nested Disctionaries

students = {
    'students1':{'name':"manish",'age':32},
    'students2':{'name':"anish",'age':22}
}

print(students)

### Access nested dictionaries elementss
print(students['students1']['name'])
print(students['students2']['name'])

students.items()

### Iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")