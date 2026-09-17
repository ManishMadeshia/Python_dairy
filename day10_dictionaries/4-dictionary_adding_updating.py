#q1. Create a dictionary containing your name and age. Add a new key "city".
bio = {
    'name':'manish',
    'age':25,
}
print(bio)

bio['city'] = 'mumbai'
print(bio)

#q2.Create a student dictionary and add "course".

student = {
    'name':"manish",
    'age':'24',
}

student['course']='Data Engineer'
print(student)

#q3. Create an employee dictionary and update the salary value.

employee={
    'emp_name':"Manish",
    "emp_salary":44444
}
print(employee)

employee['emp_salary']=55555
print(employee['emp_salary'])

#q4.Create a dictionary and update the city from "Mumbai" to "Pune".
details = {
    'name':"anish",
    'city':'mumbai'
}

details['city']='pune'

#q5.Add a new key-value pair using square brackets.
details['job']='Data Engineer'
print(details)

#q6.Use update() to add two new key-value pairs.
details.update({
    'experience':'Fresher',
    'rellocation':"Yes Possible"
})

print(details)

#q7.Use update() to modify an existing key.

details.update({
    'experience':"Junior Level",
    'rellocation':"not possible"
})

print(details)

#q8.Create a dictionary containing five details, then add two more details using update().


employee = {
    "name": "Manish",
    "age": 25,
    "salary": 30000,
    'city':"mumbai",
    'job':"fresher"
}

employee.update({
    'age':26,
    'joiner':'immediate'
})

print(employee)

#q9.Perform these operations:Add "city": "Mumbai",Update salary to 35000,Add "department": "Data Engineering"

employee = {
    "name": "Manish",
    "age": 25,
    "salary": 30000
}

employee['city']='mumbai'
employee['salary']=35000
employee['department']='Data Engineering'

print(employee)

'''Q10

Create a complete program that:

Creates a student dictionary.
Adds a course.
Updates marks.
Adds city and email using update().
Prints the final dictionary.
'''

student={
    'name':"manish",
    'Marks':88,
}

student['Course']='Data Engineering'
student['Marks']=98

student.update({
    'City':"Mumbai",
    'email':"manish@gmail.com"
})

print(student)