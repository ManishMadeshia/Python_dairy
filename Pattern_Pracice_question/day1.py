'''
#q1. You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

n = int(input("Enter a number: "))

result = []
for i in range(n):
    result.append('*'*n)

print(result)


def squ_star(n):

    pattern = []
    for i in range(n):
        row =  '*' * n
        pattern.append(row)
        return pattern

squ_star(4)

#q2. You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

result = []
for i in range(n):
    if i==0 or i == n-1:
        row = ('*'*n)
        result.append(row)
    else:
        row = ('*'+" "*(n-2) +'*')
        result.append(row)

print(result)

#q3. You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).

#condition : Two integers n and m, where 1 <= n, m <= 100.
#Input: n = 4, m = 5, Output: ['*****', '*****', '*****', '*****']

n = int(input("Enter numner n: "))
m = int(input("Enter numner m: "))

rect = []
if n>= 1 and m <= 100:
    for i in range(n):
            row = '*' * m
            rect.append(row)

else: print("Error!: Please Enter numner :  n >= 1 and m <=100")

#4. You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.


n = int(input("Enter a number : "))

res = []
for i in range(n):
     row = '*' * (i+1)
     res.append(row)
print(f' Right Angle Triangle: {res}' )


#5. You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.


n = int(input("Enter a number : "))
res = []
for i in range(n):
     row = '*' * (n-i) 
     res.append(row)
print(res)

'''

#q6. You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

n = int(input("Enter Number N: "))
ress=[]
for i in range(n):
    space = ' '* (n-i-1)
    stars = '*' * (2 * i + 1)
    res = space + stars
    ress.append(res)
print(ress)


#q7. You are given an integer n. Your task is to return a right-angled triangle pattern of '*', where each row contains stars aligned to the right. The first row has one star, the second row has two stars, and so on, until the nth row has n stars.

ress = []
for i in range(1,n+1):
    space = ' '* (n-i)   
    star = '*' * i
    res = space + star
    print(res)
    ress.append(res)
print(ress)


