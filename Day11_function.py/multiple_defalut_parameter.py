#q1. def employee(name="Manish", city="Mumbai"): print both value Call it without arguments and then override both.

def employee(Name="Manish",city='mumbai'):
    print(f"{Name},{city}")

employee()
employee(Name="anish",city="Kolkata")


#q2. test different combination def employee(name, department="IT", salary=30000):

def employee(name,department="IT",salary=44444):
    print(f"{name},{department},{salary}")

employee(name="manish")

#q3. def student(name, course="Python", city="Mumbai"): call it Without optional arguments, With course, with course and city

def student(name,course = "python", city ="Mumbai"):
    print(f"{name},{course},{city}")

student(name='sejal',course="DATA ENGINEERING",city="delhi")
student(name="meehir",course='IT')
student(name="Man",course='IT',city="kolkata")


#q4. def product(name, price=1000, quantity=1):

def product(price,quantity):
    print(price*quantity)

product(33,44)

#q5. def employee(name, department="IT", salary=30000, city="Mumbai"):

def employee(name, department="IT", salary=30000, city="Mumbai"):
    print(f"{name},{department},{salary},{city}")

employee(name='Manish')
employee(name="anish",department="COMM",salary=33333,city='kolkata')
employee(department="COMM",salary=44443,city='Mumbai',name="nisha")
employee(name="Deepak",salary=99999,city="mumbai")