#Create a set of five fruits and print it.
s = {'mango','banana','chikoo','apple','kiwi'}
print(s)

#Add a new fruit using add().
s.add("dragon fruits")
print(s)

#Add three more fruits using update().
s.update(["litchi",'watermelon','jamun'])
print(s)

#Remove one fruit using remove().
s.remove('chikoo')

#Remove one fruit using discard().
s.discard("jackfruits")
print(s)

#Remove an arbitrary element using pop() and store it separately.
remove_ele = s.pop()
print(remove_ele)

#Create two sets of numbers and find their union.
s = {1,2,3,4,5}
s1 = {3,4,5,6,7}
s.union(s1)
print(s)

#Find the intersection of the two sets.
s.intersection(s1)
print(s)

#Use a for loop to print all elements of a set.
for i in s:
    print(i)

#Print only even numbers from a set.
for i in s:
    if i%2==0:
        print(i)
#Print only odd numbers from a set.
for i in s :
    if i%2==1:
        print(i)

#Calculate the sum of all numbers in a set using a loop.
sum = 0
for i in s:
    sum = sum + i
print(sum)

#Count the elements in a set using a loop.
count = 0

for i in s:
    count = count +1
print(count)

#Create a set of squares using set comprehension.
s = {i*i for i in s}
print(s)

#Create a set of cubes using set comprehension.
s = {i*3 for i in s}
print(s)

#Create a set of even numbers from 1 to 20 using set comprehension.
s = {i for i in range(1,21) if i%2==0 }
print(s)

#Given two sets of fruits, find common fruits.
fruit = {'mango','banana','chikoo'}
fruit1 = {'mango','chikoo'}

fruit.union(fruit1)
print(fruit)

#Given two sets of students, find students present in only the first set.
set_a = {"Alice", "Bob", "Charlie", "David"}
set_b = {"Charlie", "David", "Edward", "Frank"}

only_in_first = set_a - set_b
print(only_in_first)

#Convert a list with duplicate numbers into a set.
li = [1,2,3,4,3,2,1,3,4]
li = set(li)
print(li)
print(type(li))
li = list(li)
print(li)
print(type(li))

#Create an empty set and verify its datatype.
s = set()
print(s)

s = {}
print(s)

#Try accessing a set using an index and observe the error.
s= {1,2,3,4,5}
#print(s[3])
#set object are not subscriptable reason set does not follow ordering

#Create a complete program that:Starts with a set of numbers.,Adds new numbers.,Removes a number.,Finds the even numbers.,Finds the sum.,Prints the final set.

ss = {1,2,3,4,5,6}

ss.add(8)
print(ss)
ss.remove(2)
print(ss)
for i in ss:
    if i%2 ==0:
        print(ss)

sum = 0
for i in ss:
    sum = sum+i

print(sum)

print(ss)