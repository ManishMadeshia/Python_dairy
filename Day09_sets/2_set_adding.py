#1. Create a set of three fruits and add "Orange" using add().
fruits  = {'mango','banana','grapes'}
print(fruits)
fruits.add('orange')
print(fruits)

#2. Create a set of numbers {10, 20, 30} and add 40.
set = {10,20,30}
set.add(40)
print(set)

#3. Add a duplicate element to a set and observe the result.
set.add(10)
print(set)

#4. Create a set of two cities and add three more cities using update().
city = {'mumbai','delhi'}
city.update(['goa','pune'])
print(city)

#5. Use update() to add multiple numbers to an existing set.
num = {1,2,3,4,5,6}
num.update([7,8,9])
print(num)

#6. Add a list of fruits to a set using update().

fruits.update(['kiwi','dragon fruits','pineapple'])
print(fruits)

#7. Add a tuple of numbers to a set using update().
num.update([(5,6,7)])
print(num)

#8. Create an empty set using set(), then add five elements one by one using add().
#s = set()
#s.add([1,2,3,'manish',33.2])
#print(s)

#9. Create a set of numbers and use update() to add another set of numbers.
s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}

s1.update(s2)
print(s1)

#10. Add 4 using add(), then add 5, 6, 7 using update(), and print the final set.
numbers = {1, 2, 3}

numbers.add(4)
numbers.update([5,6,7])
print(numbers)