#predict output

a = 17
b = 5

print(a / b) #3.something
print(a // b) #3
print(a % b) #2
print(a ** 2) # 289


#Explain why the comparison results are what they are.
a = 10
b = 10.0
c = "10"

print(type(a)) #int
print(type(b)) #float
print(type(c)) #str
print(a == b) # true reason a is int, b is float 
print(str(a) == c) #try


#track the value of x after every statement

x = 20
x += 5 #25
x *= 2 # x = x * 2 = 50
x -= 10 # 40
x //= 3 #13

print(x)

#boolean logic
a = 8
b = 12

print(a > 5 and b < 10) #true and false = false
print(a > 5 or b < 10) # true or false = true
print(not (a == 8)) # not true = false
print(a != b and b % 2 == 0) # true and true = true

#type conversion
#Explain the difference between numeric addition and string concatenation.


a = "25"
b = 5

print(int(a) + b) # 30
print(a + str(b)) #255
print(float(a) / b) # 4.0

# in numeric addition we can perform all operation addition, subtract but in string we can if the value is in integer and ecnclosed in string brace convert it into int datatype then only we can do


#What is wrong with this code, and how would you correct it?
#age = input("Enter your age: ")
#print(age + 5)

#corrected code 
age = int(input("Enter your age: "))
print(age + 5)
#input by default take the value in string so we cant add str and int together to get byproduct first we have to do the input which we are taking convert it into str then we can do all operaiton


#Predict the output or identify the error in each expression:

print(10 + 2.5) #12.5
print("10" * 3) #101010
#print("10" + 3) #error addition not work dues to string and int concat
print(bool(0)) # false
print(bool("False")) #true

#swapping varibale : Swap the values of a and b without using a third variable.Swap the values of a and b without using a third variable.

a = 15 
b = 25
a,b = b,a
print(a)
print(b)

'''
Q10. Calculate a bill
A customer buys three products priced at ₹250, ₹399, and ₹151. Apply a 10% discount to the total.
Write a program that calculates and prints:
- Original total
- Discount amount
- Final amount
Use variables and arithmetic operators.
'''

product_1 = 250
product_2 = 399
product_3 = 151


print(f"Original Total Amount: {product_1+product_2+product_3}")
print(f"Discount Amount : {(product_1+product_2+product_3) * 0.10}")
print(f"Final Amount: {(product_1+product_2+product_3) * 0.90}")

#For is, explain the difference between object identity and value equality.

x = 15
y = 20
z = 15

print(x == z) # True
print(x is z) # False
print(x != y) # True
print(x < y <= 25) # True

#object identity refer to value present at same location and value equality value present at different location conatining same value

#Evaluate each operation in the correct order.
x = 18
y = 6
z = 3

result = x > y * z and y % z == 0 or x // y == 3
print(result)

#Q13. Membership operators

text = "DataEngineering"
numbers = [10, 20, 30, 40]

print("Data" in text) #true
print("data" in text) #false
print(20 in numbers) #true
print(50 not in numbers) # true

#Why does capitalization matter in the string comparisons
#-----beacuse computer process text as a sequence of numbers and uppercase and lowercase letter are assigned different numeric values in characeter


'''
Q14. Calculate average
A student scores 78, 85, 92, and 65 in four subjects.
Write a program to calculate the average and determine whether it is at least 80.
Expected output format:
'''

sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 65

greater_than_80 = 80
total_marks = sub1+sub2+sub3+sub4
avgs = total_marks / 4
print(f"The average of 4 subject is : {avgs}")
print(f"Wheather avg greater than 80 : {greater_than_80 >= avgs}")

'''
Q16. Time conversion
A program receives a duration of 9876 seconds.
Calculate the number of complete hours, remaining minutes, and remaining seconds using // and %.
'''

total_sec = 9876

Hours = total_sec // 3600
remainig_second = total_sec % 3600
minutes = remainig_second // 60
seconds = remainig_second % 60


print("Hours:", Hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

'''
An employee earns a monthly basic salary of ₹35,000. The employee receives a housing allowance of 20% of basic salary and a travel allowance of ₹2,500.
Calculate:
- Housing allowance
- Total monthly salary
- Annual salary
'''

salary = 35000
travelling_allowance = 2500
housing_allowance = salary * 0.20

monthly_salary = salary + travelling_allowance + housing_allowance
annual_sal = monthly_salary * 12

print(f"Monthly Housing Allowance: {housing_allowance}")
print(f"Total Monthly Salary : {monthly_salary}")
print(f"Annual Salary: {annual_sal}")

'''
Q18. Distance conversion
A vehicle travels 125.5 kilometres. Convert this distance into metres and miles.
Use:
- 1 kilometre = 1,000 metres
- 1 kilometre ≈ 0.621371 miles
Round the miles result to two decimal places.
'''

total_travel_km = 125.5
total_travel_km_in_meter = 125.5*1000
total_travel_km_in_miles = round(total_travel_km * 0.621371,2)

print(total_travel_km)
print(F'The total km in meter:{total_travel_km_in_meter}')
print(f'The total km in miles: {total_travel_km_in_miles}')


'''
Q19. Debugging challenge
The following code is intended to calculate the average of three numbers and check whether it is greater than 50.
Find and fix all issues.

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

average = a + b + c / 3

print("Average:", average)
print("Above 50:", average > "50")
'''

a = int(input("Enter first number: "))  #correction was input value which was in str type we want int
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = a + b + c / 3

print("Average:", average)
print("Above 50:", average > 50)

'''
20. Mini project — Shopping calculator
Write a program for a shopping order with these requirements:
- Product price: ₹1,250
- Quantity: 4
- Discount: 12% of the subtotal
- Delivery fee: ₹100
- GST: 18% on the discounted subtotal
Calculate and display:
1. Subtotal
2. Discount
3. Taxable amount after discount
4. GST
5. Final payable amount, including delivery
State clearly whether GST is applied to the discounted subtotal or to the subtotal before discount.
'''

Product_price = 1250
Quantity = 4
Delivery = 100

Subtotal = 1250 * Quantity
Discount = Subtotal * 0.12
Amount_after_discount = Subtotal - Discount
GST = Amount_after_discount * 0.18
Final_amount = Amount_after_discount + Delivery + GST

print(f"Subtotal Amount: {Subtotal}")
print(f"Discount @ 12%: {Discount}")
print(F"Taxable Amount After discount: {Amount_after_discount} gst not applied")
print(f'GST : {GST}, 18% of Subtotal')
print(f"Final payable amount, including delivery & gst: {Final_amount}")