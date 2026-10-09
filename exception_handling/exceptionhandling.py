
'''
    try :
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))

    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")



try :
    num = int(input("enter a num: "))
    print(f"the number enter by user is {num}: ")
except:
    print("Please Enter a valid number")



#Ask the user for an index and print the value at that index.
numbers = [10, 20, 30, 40, 50]

try :
    idx = int(input("Enter a index number you want to find: "))

    print(numbers[idx])
except IndexError:
    print(f'Enter a correct index number between 0 and {len(numbers)-1} ')
except ValueError:
    print("Error: Please enter a valid integer, not text or decimals.")



student = {
    "name": "Manish",
    "age": 25,
    "course": "Data Engineering"
}

try:
    keys = input("enter a key : ")
    print(student[keys])
except KeyError:
    print("key does not exist")



try :
    a = int(input("enter a num1: "))
    b = int(input("enter a num2: "))

    result = a/b
    print(f'the division of two number is {result}')

except ZeroDivisionError:
    print("Error: Cant divide by zero")
except ValueError:
    print("Error: Enter a valid No")


try:
    num = int(input("Enter a Number: "))
except ValueError:
    print("Error : Enter a valid no")
else:
    print(f"Valid Number: {num}")



try :
    num1 = int(input("enter a num1:"))
    num2 = int(input("enter a num2:"))
    result = num1/num2
except ZeroDivisionError:
    print("Error: Value Cannot divide by zero")
except ValueError:
    print("Error: Enter a valid number")
else:
    print(result)
finally:
    print("Program execution completed")


try:
    with open("employees.txt",'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")



numbers = [10, 20, 30, 40]

try:
    idx = int(input("Enter a idx number: "))
    num = numbers[idx]
    result = num/100
except ZeroDivisionError:
    print("Error: Cant divide by zero")
except IndexError:
    print("Error: Index not found")
except ValueError:
    print("Please Enter a valid index")
else :
    print(f"Result is : {result}")
finally:
    print("Execution Completed")

'''

