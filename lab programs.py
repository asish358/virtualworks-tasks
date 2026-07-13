Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in rnage(1,11):
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    for i in rnage(1,11):
NameError: name 'rnage' is not defined. Did you mean: 'range'?
for i in range(1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
count=0
num=2
while count<10:
    print(num)
    num+=2
    count+=1

    
2
4
6
8
10
12
14
16
18
20
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("enter a number: "))
SyntaxError: invalid syntax
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
  num=int(input("enter a number: "))
  
SyntaxError: unindent does not match any outer indentation level
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
    num=int(input
    ("enter a number:"))
    print(f"the factorial of {num} is :{factorial(num)}")

    
5
5
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
    num=int(input
    ("enter a number:"))
    print(f"the factorial of {num} is :{factorial(num)}")
    5

    
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")

SyntaxError: invalid syntax
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
    num = 5
print(f"The factorial of {num} is {factorial(num)}")
SyntaxError: invalid syntax
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")

    
n=int(input("enter a value: "))
enter a value: 5
a=1
for i in range(1,n+1):
    a*=i

    
print(a)
120
num=int(input("enter a number:"))
enter a number:5
>>> for i in range(1,11,1):
...     i*=num
... 
...     
>>> print(i)
50
>>> num=int(input("enter a number:"))
enter a number:5
>>> for i in range(1,11,1):
...     i*=num
... 
...     
>>> print(i)
50
>>> print(num)
5
>>> num=int(input("enter a number:"))
enter a number:5
>>> for i in range(1,11,1):
...     i=i*num
... 
...     
>>> print(i)
50
>>> num=int(input("enter a number:"))
... enter a number:5
... for i in range(1,11,1):
...     i=i*num
...     print(i)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> num=int(input("enter a number:"))
... enter a number:5
... for i in range(1,11,1):
...     i=i*num
...     print(i)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> num=int(input("enter a number: "))
enter a number: 5
>>> for i in range(1,11,1):
...     i=i*num
...     print(i)
... 
...     
5
10
15
20
25
30
35
40
45
50
