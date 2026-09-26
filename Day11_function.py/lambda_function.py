#q1.Create a lambda function to add two numbers.

add_num = lambda a,b : a+b
print(add_num(2,3))

#q2. Create a lambda function to subtract two numbers.

sub_num = lambda a,b : a-b
print(sub_num(3,2))

#q3. Create a lambda function to multiply two numbers.

mul_num = lambda a,b : a*b
print(mul_num(3,2))

#q4.Create a lambda function to divide two numbers.

div_num = lambda a,b : a/b
print(div_num(3,2))

#Create a lambda function to find the square of a number.

squ_num = lambda a,b:a*b
print(squ_num(3,4))

#6.Create a lambda function to find the cube of a number.

cub_num = lambda a:a**3
print(cub_num(4))

#7.Create a lambda function that checks whether a number is even or odd.

check_num = lambda num: "even" if num%2==0 else "odd"
print(check_num(4))

#8.Create a lambda function that returns the larger of two numbers.
larg_num = lambda a,b : "a is larger" if a>b else "b is larger "
print(larg_num(4,3))

#9. Create a lambda function that calculates the area of a rectangle.
area_rect = lambda l,b: l*b
print(f'the area of rectangle is : {area_rect(4,3)}')

#q10. Create a lambda function that accepts: name, salary, bonus, and reurn saalry + bonus

func = lambda name,salary, bonus : salary + bonus

print(func("Manish",35000,3222))