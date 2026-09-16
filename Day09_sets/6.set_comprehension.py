#Q1. Create a set containing squares of numbers from 1 to 5.
num = {i**2 for i in range(1,6)}
print(num)

#q2. Create a set containing cubes of numbers from 1 to 5.
cub = {i**3 for i in range(1,6)}
print(cub)

#q3. Create a set of even numbers from 1 to 10.
even_num = {i for i in range(1,11) if i%2==0 }
print(even_num)

#q4. Create a set of odd numbers from 1 to 10.
odd_num = {i for i in range(1,11) if i%2==1 }
print(odd_num)

#q5.Create a set containing numbers greater than 5 from an existing set.
nums = {i for i in num if i>=5}
print(nums)

#q6.Convert a set of names into uppercase names.
names = {'manish','bipin','rohit','rani'}
for name in names:
    print(name.upper())

#q7. Create a set containing the lengths of words from another set.

len_word = {len(name) for name in names}
print(len_word)

#q8. Create a set of numbers divisible by 3 from 1 to 20.

s = {i for i in range(1,21) if i%3 ==0}
print(s)

#q9. Given {1, 2, 3, 4, 5}, create a set containing double of every number.
num = {1, 2, 3, 4, 5}
double = {n+n for n in num }
print(double)

#q10. Create: A set of even numbers. A set of odd numbers. A set of numbers greater than 20. A set containing squares of all numbers.

numbers = {10, 15, 20, 25, 30, 35}

even = {num for num  in numbers if num%2==0}
print(even)

odd = {num for num  in numbers if num%2==1}
print(odd)

s = {s for s in numbers if s>20}
print(s)

squ = {s*2  for s in numbers }
print(squ)