# A simple program to greet the user and check an input number

def check_number(num):
    if num % 2 == 0:
        return f"{num} is Even!"
    else:
        return f"{num} is Odd!"

# Test the function
user_num = int(input("Enter a number: "))
print(check_number(user_num))
