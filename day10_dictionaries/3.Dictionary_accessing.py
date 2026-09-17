#q1. Create a dictionary containing your name, age, and city. Print the value of each key using [].

bio = {
    'name':"Manish",
    'age':25,
    'city':"mumbai"
}
print(bio['age'])
print(bio['city'])
print(bio['name'])

#q2. Create a student dictionary and print the course using square brackets.
student = {
    'name':'manish',
    'course':"data engineering bootcamp"
}

print(student['course'])

#q3,Create a dictionary of employee details and access the salary value.

employees={
    'name':"manish",
    "job" : "data engineer",
    'salary': 45000

}

print(employees['salary'])

#q4.Use get() to access the "name" value from a dictionary.
print(employees.get('name'))
print(employees.get('salary',35000))

#q5.Use get() to access a key that exists.

print(employees.get('name'))

#q6.Use get() to access a key that does not exist and observe the result.
print(employees.get('expericence'))

#Q7.#Use get() with a default value for a missing key.
print(employees.get('expericence','mid-level')) #passing default value

#q8.Create a dictionary containing five key-value pairs and access at least three values using [].

resume = {
    'name':"Manish",
    'age':25,
    'city':"mumbai",
    'relocation':"ready to rellocate",
    'expected_salary':60000
}

print(resume['age'])
print(resume['expected_salary'])
print(resume['relocation'])

'''#q9.Create a dictionary and compare the result of:
dictionary["missing_key"]
and
dictionary.get("missing_key")'''

student = {
    "name": "Manish",
    "age": 25
}

# Using square brackets
#print(student["phone"]) this raise a error if we direct access the value and it is not present

student = {
    "name": "Manish",
    "age": 25
}

# Using get()
print(student.get("phone")) #using get it is method using which it will not raise error if value not present and print none
print(student.get('phone','Not Available')) #default value



'''q10.Print:

Name using []
Age using get()
Department using []
Salary using get()
A missing key using get() with "Not Available" '''

employee = {
    "name": "Manish",
    "age": 25,
    "department": "Data Engineering",
    "salary": 35000
}

print(employee['name'])
print(employee.get('age'))
print(employee['department'])
print(employee['salary'])
print(employee.get('job','not available'))