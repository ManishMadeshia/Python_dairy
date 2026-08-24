#Remove Mango.
li = ['banana','mango']
li.remove('mango')
print(li)

#Remove Mumbai.

li = ['jaipur','mumbai']
li.remove('mumbai')
print(li)

#Remove number 20.
n = [33,22,44,22,1,20]
n.remove(20)
print(n)

#Pop last element.

n = [33,22,44,22,1,20]
n.pop()
print(n)

#Pop first element.

n.pop(0)
print(n)


#Remove employee name.
emp_name = ['manish','khushboo','dinesh','bipin']
emp_name.remove('manish')
print(emp_name)

#Clear entire list.
emp_name.clear()
print(emp_name)

#Remove a color.
color = ['blue','green','black']
color.remove('blue')
print(color)

#Remove city and print remaining list.

cities = ["Paris", "Tokyo", "London", "New York"]
city = input("enter city name to remove: ").title()

cities.remove(city)
print(cities)

#Remove two elements from list.
emp_name = ['manish','khushboo','dinesh','bipin']
index = 1
index = 3

emp_name_to_remove = emp_name[index]
emp_name.remove(emp_name_to_remove)
print(emp_name)