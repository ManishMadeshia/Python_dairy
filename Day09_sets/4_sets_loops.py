#q1. Create a set of five fruits and print each fruit using a for loop.

fruits = {'mango','banana','grapes','chikoo','pineapple'}

for fruit in fruits:
    print(fruit)

#q2. Create a set of numbers and print each number.
num = {1,2,3,4,5}
for i in num:
    print(i)

#q3. Print only even numbers from a set.
for i in num:
    if i%2==0:
        print(i)

#q4. Print only odd numbers from a set.
for i in num:
    if i%2==i:
        print(i)

#q5. Print numbers greater than 10 from a set.

num={10,22,1,2,3,22,11,222}

for i in num:
    if i > 10:
        print(i)

#q6.Print numbers less than or equal to 20.

for i in num:
    if i <=20:
        print(i)

#q7.Create a set of names and print "Hello" before each name.

names = {"manish","khushboo","Dinesh"}
for name in names:
    print(f"Hello {name}")

#q8.Count the number of elements in a set using a loop.
count = 0
for i in names:
    count  = count +1
print(count)

#q9. Find the sum of all numbers in a set using a loop.
sum = 0
num = {1,2,3,22,344,66,55,7}

for i in num:
    sum = sum +i
print(sum)

#q10. Given  Using a loop: Print even numbers.Print odd numbers.Calculate the sum. Count the total elements.

numbers = {5, 10, 15, 20, 25, 30}

for i in numbers:
    if i %2 ==0:
        print(i)
print("even number ends here")

for i in numbers:
    if i %2 ==1:
        print(i)
print("even number odds here")


sum = 0

for i in numbers:
    sum = sum + i
print(f"the total sum of numbers is {sum}")


count = 0

for i in numbers:
    count = count + 1
print(f"the total count of numbers is {count}")
