'''
Problem Description:

You are given a temperature in Celsius.
Your task is to convert it to Fahrenheit and return the result.

Formula: To convert Celsius to Fahrenheit, use the formula:
 F = (9/5 * C) + 32

Where F is the temperature in Fahrenheit and C is the temperature in Celsius.
'''

#sol 

def temp(temp):
    return (f"The Temperature in Fahrenheit is : {((9/5 * temp) + 32)}")

print(temp(32.2))


"""
Problem Description:

You are given the length and breadth of a rectangle. Your task is to compute and return the area of the rectangle.

Formula:

To calculate the area of a rectangle:

Area=length×breadth

"""

def area_of_rectangle(length, breadth):
    return length * breadth

area_of_rectangle(3,4)



'''
Problem Description:

You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.

Formula:

To calculate the distance traveled by a vehicle:

Distance=Speed×Time
'''

def cal_distance(speed,time):
    return (f"Total Distance Travel : {speed * time}")

print(cal_distance(65.0,1.5))


'''
You are given n, the total number of people,
 and capacity, 
 the maximum number of people the lift can carry at a time. 
 All people want to go from the ground floor to the top floor. 
 Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.

'''


round = 0
n = 12
capacity = 2
while n > 0:
    n = n - capacity
    round = round +1 

print(round)


def lift_round(n,capacity):
    round = 0
    while n >0:
        n = n -capacity
        round = round + 1
    return round

print(lift_round(33,5))

'''
You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:

'''

def calculate_y(m,b,x):
    y = m*x+b
    return y

print(calculate_y(3,4,2))