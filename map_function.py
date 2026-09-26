#q1. numbers = [1, 2, 3, 4, 5] Use map() and lambda to double every number.

numbers = [1, 2, 3, 4, 5]

double_num = map(lambda number: number + number,numbers)
print(list(double_num))

#q2. Use map() to find the square of: 
numbers = [2, 4, 6, 8, 10]

squ = map(lambda number:number * number , numbers)
print(list(squ))

#q3. use map to find square of every number
numbers = [2, 4, 6, 8, 10]
cube = map(lambda number : number **3 , numbers)
print(list(cube))

#q4. Use map() to add 5 to every number.
numbers = [10, 20, 30, 40]

add_5 = map(lambda number:number +5 , numbers)
print(list(add_5))

#q5. Use map() to subtract 5 from every number.

sub_5 = map(lambda number:number - 5,numbers)
print(list(sub_5))

#q6. convert it to uppercase
names = ["manish", "rahul", "amit", "priya"]

upp_names = map(lambda name: name.upper(),names)
upp_names = list(upp_names)
print(upp_names)

#q7. uppercase to lowercase

lower_case = map(lambda upp_name: upp_name.lower(),upp_names)
print(list(lower_case))

#q8. Use map() with a normal function to return "Even" or "Odd" for every number.
numbers = [1, 2, 3, 4, 5]

def check_num(numbers):
    if numbers%2==0:
        return "even"
    else:
        return "odd"

new_num = map(check_num,numbers)
print(list(new_num))


#q9. Use map() to add 18% GST to every price.
prices = [100, 200, 300, 400]

new_price = map(lambda price : price + price*0.18,prices)

print(list(new_price))

#q10. Use map() and a lambda function to create a list containing only the salaries.
employees = [
    ("Manish", 35000),
    ("Rahul", 40000),
    ("Amit", 45000)
]

salaries = map(lambda employee:employee[1],employees)
print(list(salaries))