#q1. Create a set of fruits and remove "Mango" using remove().
fruits = {'mango','banana','chikoo'}
fruits.remove('mango')

#q2. Create a set of numbers and remove one number using remove().

num = {1,2,3,4,5,7}
remove_num = num.pop()
print(remove_num)
print(num)

#q3. Try removing an element that does not exist using remove() and observe the error.
#num.remove(10) #if we use remove and number is not present that it will throw error

#q4. Use discard() to remove an existing element.
num.discard(4)

#q5. Use discard() to remove a non-existing element without causing an error.

num.discard(100)
print(num)

#q6.Create a set of cities and remove one city using pop().
city = {'california','goa','toronto','nepal'}
remove_city = city.pop()
print(remove_city)
print(city)

#q7.  Print the element removed by pop().
city = {'california','goa','toronto','nepal'}
remove_city = city.pop()
print(remove_city)

#q8. Create a set of five numbers and remove all elements using repeated pop() calls.

number = {1,2,3,4,5}
while number:
    num_pop = number.pop()
    print(num_pop)
print(number)

#q9. fruits = {'mango','banana','chikoo'}

fruits.clear()
print(fruits)

#q10. given numbers = {10, 20, 30, 40, 50}

#Perform these operations:

#Remove 20 using remove().
#Remove 40 using discard().
#Remove one arbitrary element using pop().

number = {10, 20, 30, 40, 50}
number.remove(20)
number.discard(40)
rem= number.pop()
print(number)
print(rem)
