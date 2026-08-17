
'''
#Q1.Take age as a string: age = "25" Convert it into integer and print its datatype.

age = 25
age_str = str(age)
print(type(age_str))

#Q2. convert salary = "35000.50" into float and print the datatype.

salary = 35000.50
salary_float = float(salary)
print(type(salary_float))

#Q3. convert num = 100 into string and print the datatype.

num = 100
num_str = str(num)
print(type(num_str))

#Q4. price = 99.99 Convert it into integer and print the result.

price = 99.99 
price_int = int(price)
print(type(price_int))
print(price_int)

#Q5. Take two strings: a = "10", b = "20" Convert them into integers and print their sum.

a = "10"
b = "20"

a_int = int(a)
b_int = int(b)

print(a_int)
print(b_int)
print(a_int+b_int)

#6 take weight = '81.5' Convert it into float and multiply by 2.

weight = '81.5'
weight_float = float(weight)
print(type(weight_float))
print(weight_float * 2)

#7. Take input from user for age and convert it into integer.

age = int(input("Enter Age: "))
print(type(a))
age_int = int(age)
print(age_int)
print(type(age_int))

#8. Take input for salary and convert it into float.

salary = int(input("enter ur salary: "))
print(type(salary))
salary_float = float(salary)
print(salary_float)
print(type(salary_float))

'''

#Q1 Check if age is greater than 18.
age = 18
if age > 18:
    print("Adult")

#2 Check if salary is greater than 30000. 
salary = 30000
if salary > 30000:
    print("high income")

#3. Check whether a number is even or odd.

num = int(input("enter a num: "))
if num %2==0:
    print("even")
else:
    print('odd')

#4. Check whether age is eligible for voting.

age = 22

if age > 18:
    print("eliglible")
else:
    print("Not eliglible")

#5 Check whether salary is greater than 50000.

salary = 50000

if salary > 60000:
    print("greater")
else:
    print("not greater")

#6. Grade System 90+ → A 75–89 → B 60–74 → C Below 60 → Fail

mark = int(input("enter a marks: "))

if mark > 100 or mark < 0:
    print("Invalid marks entered")
elif mark>=90:
    print("Grade: A")
elif mark>= 75:
    print("Grade : B")
elif mark>= 60:
    print("Grade : C")
else:
    print("Grade: Fail")
#7. Check age category Below 13 → Child 13–19 → Teenager 20–59 → Adult 60+ → Senior Citizen


age = int(input("enter your age: "))


if age > 60:
    print("senior")
elif age >= 20:
    print("Adult") 
elif age >= 13:
    print("teenager")
else:
    print("child")



#8 Check temperature 40 → Very Hot , 30–40 → Hot, 20–29 → Normal ,Below 20 → Cold

temp = int(input("Enter temperature : "))

if temp > 40:
    print("Very hot")
elif temp >=30 :
    print("Hot")
elif temp >= 29:
    print("Normal")
else:
    print("cold")

#9. Check experience 0–1 → Fresher, 2–4 → Junior, 5–8 → Mid Level, 9+ → Senior

exp = int(input("Enter your Experience: "))

if exp <= 1:
    print("Fresher")
elif exp <= 4:
    print("Junior")
elif exp <=8:
    print("Mid Level")
else:
    print("senior")


#10. Check marks 90+ → Distinction 70–89 → First Class 50–69 → Second Class Below 50 → Fail

mark = int(input("Enter Marks: "))

if mark > 100 or mark < 0:
    print("Invalid Marks entered")
elif mark >= 90:
    print("Distinction")
elif mark >= 75:
    print("First Class")
elif mark >=60:
    print("Second Class")
else:
    print("Fail")