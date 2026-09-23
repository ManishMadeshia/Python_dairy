#q1. create def greet(name="Manish"): Call it with and without an argument.

def greet(name="manish"):
    print(f"Hello {name}")

greet("Man")
greet()


#q2. Create: def city(name="Mumbai"): Call it with and without an argument.

def city(name="Mumbai"):
    print(f"Welcome to {name}")

city("Vodara")

#q3. def salary(amount=30000):Return the salary.

def salary(amount = 30000):
    return amount
print(salary())

#q4. def country(name="India"):Return the salary. Call it with and without an argument.

def country(name="India"):
    print(f'the country name is : {name}')

country("Indo")

# create def bonus(amount=5000): Return the bonus and test it with and without an argument.

def bonus(amount=23333):
    return (f'the bonus amount:{amount}')

print(bonus(2345678))