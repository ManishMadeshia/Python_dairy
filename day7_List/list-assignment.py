
#create a list of the first 20 positive integer . ptint the list
li = []

for i in range(1,21):
    li.append(i)

print(li)

#print first, last, and middle element

print(li[0])
print(li[-1])
print(li[len(li)//2])

#print the first five element the last five element and the element from index 5 to 15 of the list created in assignemtn 1

print(li[0:5])
print(li[-1:-6:-1])
print(li[5:16])

# create a new list contaning the square of the first 10 positive integer using a list comprehnsion print the new list
new_li = [i**2 for i in range(1,11)]
print(new_li)

#create a new list containing only the even number from the list created in assignment 1 using a list comprehnshion
even_li = [i for i in li if i%2==0]
print(even_li)

#create a list of random number and sort it in asc and desc order. remove the duplicate from the list and print the modified list
import random
random_num = [random.randint(1,50) for i in range(10)]
print(random_num)
asc_random_num = random_num.sort()
desc_random_num = random_num.sort(reverse=True)
unique_num = list(set(random_num))
print(unique_num)

#create a nested list of 3*3 ,atrix and print the matrix access and print thr element at the second row and third column

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
for row in matrix:
    print(row)

print(f"element at second row and third column: {matrix[1][2]}")

#create a list of dictinaries where each dictionary represent a student with keys and score sort the list of dictonaires by the score in  desc order and print the sorted list.
