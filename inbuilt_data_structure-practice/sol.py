#Problem Description: Sum of List Elements Write a Python function that calculates the sum of all elements in a given list of integers.

numbers = [1,2,3,4,5,6,7,8,9]


def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

print(sum_list(numbers))


#Largest Element in a List : Find the Largest Element in a List : Write a Python function that finds and returns the largest element in a given list of integers.

numbers = [-12, -45, -7, -89, -23]

def largest_num(numbers):
    large = numbers[0]
    for i in numbers:
        if i > large :
            large = i
    return large

print(largest_num(numbers))

#3. Remove Duplicates from a List You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

lst = [1,2,2,3,3,3,4,4,5,8,7,6,5,5]

new_list = []

for i in lst:
    if i in new_list:
        continue
    new_list.append(i)
print(new_list)

#4. Check if all elements in a list are Unique Check if All Elements in a List are Unique You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.


lst = [1, 2, 3, 4, 5]
#lst = [1, 2, 3, 3, 4, 5]

if len(lst) == len(set(lst)):
    print(True)
else :
    print(False)

def unique_ele(lst):
    if len(lst) == len(set(lst)):
        return True
    else :
        return False

unique_ele(lst)

#Program to Reverse a List : Reverse a List (Non-Slicing Approach) You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]). The program should return the reversed list.

'''
Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
'''

reversed_list = []

lst = [1,2,3,4,5,6,7]
while len(lst) > 0:
    ele = lst.pop()
    reversed_list.append(ele)

print(reversed_list)

#Count Number of Odd and Even Elements in a List Count Even and Odd Numbers in a List You are given a list of integers. Write a Python program that counts and returns the number of even and odd numbers in the list.

'''Returns:

A tuple (even_count, odd_count) where even_count is the number of even numbers and odd_count is the number of odd numbers.'''
lst = [1,2,3,4,5,6,7,8]

even = 0
odd = 0

for i in lst :
    if i%2 == 0:
        even = even + 1
    else :
        odd = odd + 1

print(odd)
print(even)

tup_res = tuple([odd,even])
print(tup_res)


def count_even_odd(lst):
    odd = 0
    even = 0
    for i in lst:
        if i%2==0:
            even = even + 1
        else :
            odd = odd +1

    return odd, even

lst = [1,2,3,4,5,6,7,8]
count_even_odd(lst)

print(tuple([odd,even]))

#Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach) You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.


lst = [1, 7, 3, 10, 5,6,4,7,89,766,46,8,999]
max_diff = 0
for i in range(len(lst) -1):
    diff = abs(lst[i] - lst[i+1])
    if diff > max_diff:
        max_diff  = diff
print(max_diff)


def max_diff(lst):
    max_diff = 0
    for i in range(len(lst)-1):
        diff = abs(lst[i]-lst[i+1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

#Merge Two Sorted Lists : You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order.

lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8,10]


new = lst1 + lst2 
new.sort()
print(new)

def merge_two_sorted_lists(list1, list2):
    # Your code goes here
    new = list1+list2
    new.sort()
    
    return new

print(merge_two_sorted_lists(lst1,lst2))