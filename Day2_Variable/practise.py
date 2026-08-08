#Q1 Create 3 varibale (a,b,c) with values 10,20.5 and 'python" and print their data type

a = 10
b = 20.5
c = "manish"

print(type(a))
print(type(b))
print(type(c))

#Q2. swap the values of two variable without usnig a third varibale

a = 10
b = 23


print(f"the value of a is {a}")
print(f"the value of b is {b}")

a,b = b,a 
'''using the concept of swapping in python we can swap the two value without creating third variable'''
print(f"the value of a is {a}")
print(f"the value of b is {b}")

#Q3. Take input for your name and age, and print: "My name is X and I am Y years old."

name = input("enter ur name : ")
age = input("Enter ur Age: ")
print(f"my name is {name} and im {age} years old")