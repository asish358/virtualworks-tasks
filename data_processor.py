# Simple script to greet and add numbers

def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

# Run the functions
user_name = "Ashish"
print(greet(user_name))

num1, num2 = 10, 25
print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")
