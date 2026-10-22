#Problem Description: You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...


total = 0
n =5
for i in range(1,n+1):
    total = total + 2*i
print(total)

def sum_of_even_number(n):
    total = 0

    for i in range(1,n+1):
        total = total + 2*i 

    return total

print(sum_of_even_number(4))


#You are given an integer n. Your task is to check whether the number is even or not. Return True if the number is even, and False otherwise.

n = 7

if n%2 == 0:
    print(True)
else :
    print(False)

def check_even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(check_even(7))

#You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself. Return True if the number is prime, and False otherwise.

