fruits = ['banana','chikoo','guava','kiwi','oranges']

#Change first fruit to Mango.
fruits[0] = 'mango'
print(fruits)

#Change last fruit to santara.
fruits[-1] = 'santara'
print(fruits)


li = [1,33,22,44,55]
#Update second number in a list.
li[1]= 2
print(li)

#Replace city Mumbai with Pune.
cities = ['mumbai','delhi','rajkot']
if 'mumbai' in cities:
    index_to_replace = cities.index('mumbai')
    cities[index_to_replace] = 'pune'
print(cities)

#Replace mark 70 with 90.

marks = [70,55,66,55,77,90]
if 70 in marks:
    index_to_replace = marks.index(70)
    marks[index_to_replace] = 90
print(marks)

#Update first and last element.

marks[0] = 55
marks[-1] = 90

print(marks)

#Change employee name in a list.
emp_names = ['manish','birju','dj','pavan']

old_name= input("Enter a old name")
new_name = input("Enter a new name: ")

if old_name in emp_names:
    idx = emp_names.index(old_name)
    emp_names[idx] = new_name

print(emp_names)

#Modify a list of colors.

colors = ['red','blue','green','yellow']

old_color = input("Enter old color: ")
new_color = input("enter new color: ")

if old_color in colors:
    idx = colors.index(old_color) #getting index no
    colors[idx] = new_color
print(colors)


#Create list and update all elements one by one.

salary = [1000,2000,3000,4000]

for i in range(len(salary)):
    update_salary = salary[i] + 500
    salary[i] = update_salary
    print(f'updated index {i} to : {salary[i]}') 

print("\nfinal updated list: ", salary)