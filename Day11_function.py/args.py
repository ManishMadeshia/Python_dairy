#q1. Create add_all(*numbers) that returns the sum.

def add_all(*numbers):
    return sum(numbers)

print(add_all(1,2,3,43,5,7,9,4))

#q2. multiply all number

def mult_all(*number):
    result = 1

    for num in number:
        result = result* num

    return result
print(mult_all(1,2,3,4))


#q3. find maximum 

def find_max(*numbers):
    maxx = 0

    for num in numbers:
        if num > maxx:
            maxx = num
    return maxx
print(find_max(2,3,5,7,3))

#q4.
def find_min(*numbers):
    min = numbers[0]

    for num in numbers:
        if num < min:
            min = num
    return min
print(find_min(2,3,5,7,3))

#q5. count number

def count_num(*number):
    count = 0
    for num in number:
        count = count+1

    return count
print(count_num(2,3,45,6,8,5,43,2))

#Q6. print name

def print_names(*names):
    for name in names:
        print(name)

print_names("manish","deepak","dinesh")

#q7. Q7 — Sum only even numbers

def sum_even(*numbers):
    sum = 0
    for num in numbers:
        if num%2==0:
            sum = sum + num

    return sum

print(sum_even(1,2,3,4,5,7,4))

#q8. average num 

def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(1,2,3,4,5,6,6))


#q9.Q9 — String lengths

def string_len(*names):
    for name in names:
        print(name, ":",len(name))

string_len("Manish", "Rahul", "Priya")