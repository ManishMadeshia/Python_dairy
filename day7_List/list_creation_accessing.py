#Create a list of 5 fruits and print it.
fruits = ["Apple", "Banana", "Mango","guava","grapes"]
print(fruits)

#Create a list of 5 numbers and print it.
nums = [1,2,3,4,5]
print(nums)

#Print the first element from a list.
print(nums[0]) #print first element

#Print the second element from a list.
print(nums[1])

#Print the last element using negative indexing.
print(nums[-1])

#Print the third element from a list.
print(nums[2]) 

#Create a list of cities and print the first and last city.
cities = ['mumbai','pune','bangalore','dubai','berlin']
print(cities[0])
print(cities[-1])

#Create a list of marks and print the highest mark manually using indexing.
marks = [67,88,55,88,66,56,98]
marks.sort()
print(marks)
print(marks[-1]) #highest marks

#Create a list of colors and print each element using indexing.
colors = ['red','blue','green','yellow','pink']

for index, color in enumerate(colors):
    print(index,color)

for i in range(len(colors)):
    print(i,colors[i])

#Create a list containing integer, float and string and print all elements.

li = [11,22.3,'manish']
print(li)