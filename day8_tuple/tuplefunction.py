#Q1. Find the number of elements using len().
fruits = ("Mango", "Banana", "Kiwi", "Grapes", "Apple")

print(len(fruits))

#Q2. Find the maximum number using max().
numbers = (10, 25, 5, 40, 15)
print(max(numbers))

#q3. Using the same tuple, find the minimum number using min().
print(min(numbers))

#q4. Find the total using sum().
print(sum(numbers))

#q5. Calculate the average using sum() and len().
print(sum(numbers)/len(numbers))

#q6. Find how many times 10 appears using count().
count_of_10 = numbers.count(10)
print(count_of_10)

#q7. Find how many times "Apple" appears.
fruits = ("Apple", "Mango", "Apple", "Banana", "Apple")

count_of_apple = fruits.count("Apple")
print(count_of_apple)

#q8. Find the index of "Pune" using index().
cities = ("Mumbai", "Delhi", "Pune", "Jaipur", "Nashik")

indx = cities.index("Pune")
print(indx)

#Q9. Total marks ,Highest marks,Lowest marks,Average marks,Number of subjects

marks = (85, 72, 91, 64, 78, 95)

print(f'Total Marks: {sum(marks)}')
print((f'Highest Marks: {max(marks)}'))
print(f'Mininum Marks : {min(marks)}')
print(f'Average Marks: {sum(marks)/len(marks)}')
print(f"Number of subject: {len(marks)}")

#10. Find:Total salary, Highest salary, Lowest salary,Average salary

salary = (35000, 42000, 55000, 28000, 65000)

print(f'Total Salary: {sum(salary)}')
print(f'Highest Salary: {max(salary)}')
print(f"Lowest Salary: {min(salary)}")
print(f"Average Salary: {sum(salary)/len(salary)}")