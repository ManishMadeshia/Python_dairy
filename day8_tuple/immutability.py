'''#q1. Try to update element
num = (10,20,30,40,50)  #try to chnage 30 to 100 observe error

num[2] = 100

print(num)

#q2. update a string

cities = ("Mumbai", "Delhi", "Pune")
cities[2] = 'Nashik'
print(cities)

#Q3. append
fruits = ("Apple", "Mango", "Banana")
fruits.append("orange")
print(fruits) '''

#q4. tuple to list then update then tuple

numbers=(10,20,30,40)
numbers = list(numbers)
numbers[2] = 100
numbers = tuple(numbers)
print(numbers)

#q5. data = ("Manish", 25, "Mumbai") ------change manish age

data = ("Manish", 25, "Mumbai")
data = list(data)
data[1]= 26
data = tuple(data)
print(data)