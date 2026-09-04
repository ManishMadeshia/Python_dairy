#Q1. Create a list containing 5 cities and print the list.

cities = ['mumbai','pune','hyderabad','nashik','agra']
print(cities)

'''Q2. Print:

First city
Third city
Last city '''

print(cities[0])
print(cities[2]) #to access the 3 element we have to do second elememt
print(cities[-1])

#Q3. Print the last two elements using negative indexing.

print(cities[-1])
print(cities[-2])

#q4. Find the number of elements using len().

print(len(cities))

#Q5. Change "Pune" to "Nagpur".

index_to_change = cities.index('pune')
cities[index_to_change] = 'Nagpur'
print(cities)

#Q6. Add "Banana" and "Orange" using append().

new_cities = ['banana','orange']
cities.extend(new_cities)
print(cities)

#07 Insert 30 between 20 and 40

numbers = [10, 20, 40, 50]

numbers.insert(2,30)
print(numbers)

#08 Add all elements of new_numbers to numbers using extend().

numbers = [1, 2, 3]
new_numbers = [4, 5, 6]

numbers.extend(new_numbers)
print(numbers)

#09 Remove "Banana" using remove().

fruits = ["Apple", "Mango", "Banana", "Orange"]

fruits.remove('Banana')
print(fruits)


#10 Remove the last element using pop() and print the removed element.

numbers = [10, 20, 30, 40, 50]

num_pop = numbers.pop()
print(num_pop)

#11 pop by index Remove "Pune" using pop().

cities = ["Mumbai", "Delhi", "Pune", "Jaipur"]

get_index  = cities.index('Pune')
pop_elem = cities.pop(get_index)
print(pop_elem)

#12 . Create a list of 5 numbers and remove all elements using clear().

num = [1,2,3,4,5]
num.clear()
print(num)

#13. Find: Highest mark,Lowest mark, Total marks

marks = [75, 82, 91, 68, 88]

print(max(marks))
print(min(marks))
print(sum(marks))

#14. Using the same marks list, calculate the average.
sum = sum(marks)
lenn = len(marks)
print(sum/lenn)

#15. Check whether "Mumbai" exists in the list.

cities = ["Mumbai", "Pune", "Delhi", "Nashik"]

if 'Mumbai' in cities:
    print("exist",cities.index('Mumbai'))

#16. Using the same list, check whether "Bangalore" does not exist.

if "Bangalore" not in cities:
    print("Not exists")

#17. Find how many times 10 occurs.

numbers = [10, 20, 10, 30, 10, 40, 20]

print(numbers.count(10))

#18. Find the index position of "Banana".
fruits = ["Apple", "Mango", "Banana", "Orange"]
indexx = fruits.index('Banana')
print(indexx)

#19. Sort the list in ascending order.

fruits = ["Apple", "Mango", "Banana", "Orange"]
fruits.sort()
print(fruits)

#20 Using the same list, sort it in descending order.

fruits.sort(reverse=True)
print(fruits)

#21. reverse the list

cities = ["Mumbai", "Delhi", "Pune", "Jaipur"]

cities.sort(reverse=True)
print(cities)

#22. Use a for loop to print every element.

numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i,end=',')

#23. Use a for loop to create a new list containing only even numbers.
number = [12, 17, 24, 31, 40, 55, 62, 73]

even_li = []

for i in number:
    if i%2==0:
        even_li.append(i)
print(even_li)

#24. Using list comprehension, create a new list containing the squares.
numbers = [1, 2, 3, 4, 5, 6]

new = [num**2 for num in numbers]
print(new)

#25. Using list comprehension, create a new list containing only values that are not None.

data = [10, None, 25, None, 40, 55, None, 70]

new_data = [i for i in data if i is not None ]
print(new_data)