fo= []
print(fo)
print(type(fo))


# ------------solutin-----
'''
fruits = ['banana','grapes','mango','cherry','watermelon']
print(fruits)

num = [1,2,3,4,5]
print([0]) #first element
print([-1]) #last element
print([2]) #third element
print(f'the length of num is {len(num)}')


fruits.append('guava') #adding one element in last
print(fruits)

new_fruits = ['kiwi','dragon_fruits','papaya']
fruits.extend(new_fruits) #adding multiple fruits at a time
print(fruits)

fruits.insert(1,'mango')
print(fruits)

#fruits.remove('mango')

fruits.pop()
print(fruits)

#fruits.clear() clear all the list


fruits = ["apple", "banana", "cherry"]

if 'banana' in fruits:
    print("Found banana")
else:
    print("not found")


if 'banana' in fruits:
    position = fruits.index('banana')
    print(f"index of banana is {position}")


nums = [1,2,1,3,4,2,5,6,7,8,5,3,9,10]
n = int(input("enter a num u want to count (1-10)"))
countt = 0

for num in nums:
    if n==num:
        countt = countt+1
print(f'the count of num {n} is {countt}')

'''

fruits = ["apple", "banana", "cherry"]

pos = fruits.index('banana')
print(pos)

marks = [70, 85, 90, 60, 95]

print(min(marks))
print(max(marks))
print(sum(marks))
print(sum(marks)/len(marks))