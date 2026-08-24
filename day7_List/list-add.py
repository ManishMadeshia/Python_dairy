fruits = ['kiwi','banana','pistachu','grapes']

#Add Mango using append().
fruits.append("mango")
print(fruits)

#Add Orange using append().
fruits.append("orange")
print(fruits)

#Insert Apple at index 0.
fruits.insert(0,'apple')
print(fruits)

#Insert 100 at index 2.
fruits.insert(2,'100')
print(fruits)

#Add 3 cities using append().
cities = ['mumbai']
cities.extend(['jaipur','gorakhpur'])
print(cities)

cities.extend(['pune','thane','amristser'])
print(cities)

#Add multiple numbers using extend().
num = [1,2]
num.extend([3,4,5,6,7,8])
print(num)

#Insert employee name at index 1.
num.insert(1,'manish')
print(num)

#Add mark to marks list.

marks = [55,76,88,66,77]
marks.append(58) #for inserting one value
print(marks)
marks.insert(3,87) #insert value at specific location eg index(3)
print(marks)
marks.extend([76,77,98,95,55]) #insert multiple value at a time
print(marks)

#Create empty list and add 5 elements.
lst = []
lst.extend([1,2,'manish',3.22,True])
print(lst)

#Add your favorite movie to list.
movie = []
movie.extend(['3 idiot', 'kick'])
print(movie)