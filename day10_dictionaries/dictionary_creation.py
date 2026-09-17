#q1 Q1. Create a dictionary containing your name, age, and city.

bio = {'name':'manish','age':25,'city':'mumbai'}
print(bio)
print(type(bio))

#q2. Create a dictionary of a student containing:name,course,marks

student={
    'name':"Manish",
    'course':"Data Engineer",
    "marks":85
}

print(student)
print(type(student))

#q3, Create a dictionary containing five key-value pairs.

five_pairs = {
    'name':"manish",
    'age':25,
    'role':"data engineer",
    'salary':30000,
    'city':"mumbai"
}

print(five_pairs)
print(type(five_pairs))

#q4. Print the complete dictionary.
print(five_pairs)

#q5.Print the value of the "name" key.
print(five_pairs['name'])
print(five_pairs['age'])

#q6.Print the value of the "city" key.
print(five_pairs['city'])

#q7.Check the datatype of a dictionary using type().
print(type(five_pairs))

#q8.Create an empty dictionary and check its datatype.
d = {}
print(type(d))

#q9.Create a dictionary where two different keys have the same value.
new = {'name':"manish",'age':25,"city":"anish"}
print(new)

#q10.Create a dictionary containing different datatypes as values:
d = {
    'name':"manish",
    'age':24,
    "height":159.5,
    'Is_working':True
}
print(d)
print(d['Is_working'])