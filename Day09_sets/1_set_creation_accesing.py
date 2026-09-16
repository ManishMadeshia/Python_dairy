#q1. Create a Set containing 5 fruits and print it.
fruits = {'Mango','Banana','Chikoo','Apple','orange'}
print(fruits)
print(type(fruits))

#q2.Create a Set containing 5 numbers and print it.
num = {1,2,3,4,5}
print(num)

#q3. Print the Set and observe what happens to duplicate values.
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)

#q4. Create a Set containing these cities: Mumbai, Delhi, Pune, Mumbai, Delhi
cities = {"Mumbai","Delhi","Pune","Mumbai","Delhi"}
print(cities)

#q5. Check the datatype of:fruits = {"Apple", "Mango", "Banana"}

fruits = {"Apple", "Mango", "Banana"}

print(type(fruits))

#q6. Create an empty Set correctly and check its datatype.
s = {}
print(type(s))

#q7. Create a Set containing different data types: string,integer,float,boolean

s = {'manish',23,23.4,True}
print(s)

#Q8. given : numbers = {1,2,3,4,5}
 
numbers = {1,2,3,4,5}
#print(numbers[0])

#q9.Convert this List into a Set:
numbers = [10, 20, 10, 30, 20, 40]

num = set(numbers)
print(num)
print(type(num))

#q10.Convert it into a Set to remove duplicates.

data = ["Apple", "Banana", "Apple", "Mango", "Banana", "Orange"]
#Convert it into a Set to remove duplicates.

#Then convert it back into a List.

data = set(data)
print(f"data converted into set {data}")
print(type(data))

data = list(data)
print(data)
print(type(data))