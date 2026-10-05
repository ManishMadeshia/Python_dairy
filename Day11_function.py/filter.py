#q1. use filter to get only even number
numbers = [1, 2, 3, 4, 5, 6]

even_no = filter(lambda x:x%2==0, numbers)
print(list(even_no))

#q2. get only odd number

odd_no = filter(lambda x:x%2==1,numbers)
print(list(odd_no))

#q3. greater than 10

number = [5, 12, 8, 20, 3, 15]
greater = [lambda x:x>10,number]
print(greater)