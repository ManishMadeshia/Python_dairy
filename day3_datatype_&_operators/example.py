#whole number

age = 25
print(type(age))

#float number >>>>>number with decimal points
height = 5.7
price = 99.99

print(type(height))

#string - txt enclosed in quote

name = 'manish'
city = 'Mumbai'

print(type(name))

#booleam - only two value - true or false

is_student = True
print(is_student)


'''----------------Arithmetic operator--------------------'''


a = 10
b = 5


print(a+b)
print(a-b)
print(a*b)
print(a/b)  #division
print(a//b) #floor division
print(a%b)  #modulus
print(a**b) #power


#assignment operator

x = 10

x += 5  # x = x+5
print(x)

x = 20

x -=5
print(x)

x *= 2 
print(x)

x /= 3
print(x)  # x = 30//3 = 10


#comparison operator

# == equal to
# != not equal to
# > grater than
# < less than
# >= greater than or equal
# <= less than or equal

a = 10
b = 20


print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


#logical operator

age = 22
salary = 33333

print(age > 18 and salary<40000)
print(age < 22 or salary < 30000)
print(not(age>18))