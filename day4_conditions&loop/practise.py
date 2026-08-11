'''# for loop

#Q1. print number from 1 to 10

for i in range(1,11):
    print(i)


#Q2Q2. Print numbers from 10 to 1.

for i in range(10,0,-1):
    print(i)

#Q3. Print all even numbers from 1 to 20.

for i in range(1,21):
    if i%2==0:
        print(i)

#Q4. Print all odd numbers from 1 to 20.
for i in range(1,21):
    if i%2==1:
        print(i)

#Q5. Take a number from the user and print its multiplication table from 1 to 10.

num = int(input("enter a num: "))

for i in range(1,11):
    print(f'{num} * {i} = {num*i}')

#Q6. Calculate the sum of numbers from 1 to 100.

sum = 0

for i in range(1,101):
    sum = sum + i
print(sum)

#Q7. Take a number from the user and calculate its factorial.

num = int(input("enter a fac: "))
'''

'''---------------------while--------------'''

#Q1. Print numbers from 1 to 10 using while.
'''
i = 1
while i<=10:
    print(i)
    i = i+1

#Q2. Print numbers from 10 to 1 using while.

i = 10
while i > 0:
    print(i)
    i = i-1



#Q4. Calculate the sum of numbers from 1 to 100.

sum = 0

i = 1

while i <=100:
    sum = sum +i
    i = i+1
print(sum)

#Q5. Take a number and print its multiplication table using while.

num = int(input("enter a num"))

i = 1

while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i = i +1


#Q6. Keep asking the user to enter a number until they enter 0.


while True:
    n = int(input("enter a no: "))

    if n == 0:
        print("sucess! You enter a correct no")
        break
    else:
        print("sorry! please enter number again")

'''


'''--------------break--------------'''
#Q1. Print numbers from 1 to 10, but stop when the number becomes 6.

for i in range(1,10):
    if i == 6:
        break
    print(i)


#Q2. Print numbers from 1 to 20, but stop when you find the first number divisible by 7.

for i in range(1,21):
    if i % 7 == 0:
        break
    print(i)


# Q3. Keep taking numbers from the user. Stop when the user enters 0.


while True:
    num = int(input("Enter a num (enter 0 to quit)"))

    if num == 0:
        print("goodbye!")
        break


#Q4. Print numbers from 1 to 100. Stop when the number reaches 50.

for i in range(1,100):
    print(i)
    if i == 35:
        break


#Q5. Take numbers from the user continuously. Stop if the user enters a negative number.

while True:
    num = int(input("enter a num: "))

    if num < 0:
        print("no is negative")
        break

#Q6. ⭐ Create a simple password program. Give the user a maximum of 3 attempts. Stop immediately if the correct password is entered.

count = 0
passwd = 12345


while count <3:
    user_passwd = input("Enter a password: ")
    if passwd == user_passwd:
        print("Thanks for login")
    else : 
        print("please enter correct passwd")
        count = count+1
