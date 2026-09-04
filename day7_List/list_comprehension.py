#q1. Using list comprehension, create a list containing numbers from 1 to 10.

l = [i for i in range(1,11)]
print(l)


#q2. Create a list containing the squares of numbers from 1 to 10.

l = [i*i for i in range(1,11)]
print(l)

#Q3. Create a list containing the cubes of numbers from 1 to 5.

c = [i**3 for i in range(1,6)]
print(c)

#q4. Create a list containing all even numbers from 1 to 20.

l = [i for i in range(1,21) if i%2==0]
print(l)

#q5. Create a list containing all odd numbers from 1 to 20.

l = [i for i in range(1,21) if i%2==1]
print(l)

#Q6. Create a list containing the multiplication table of 5 from 1 to 10.

l = [5*i for i in range(1,11)]
print(l)

#q7. Create a new list containing only numbers greater than 50.
numbers = [10, 25, 55, 70, 32, 90, 45, 65]

new_num = [i for i in numbers if i>=50]
print(new_num)

#q8. Create a list containing the squares of even numbers from 1 to 20.

sq = [i*i for i in range(1,21) if i%2==0]
print(sq)


#q9. Create a new list containing all names in uppercase.
names = ["manish", "rahul", "amit", "rohit"]

upp_name = [i.upper() for i in names]
print(upp_name)

#Q10. Create a new list containing only temperatures greater than 30.

temperatures = [32, 28, 35, 40, 25, 30, 38]

new_tmp = [i for i in temperatures if i>=30]
print(new_tmp)

