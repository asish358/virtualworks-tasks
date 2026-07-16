Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

 





x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
True
print(x is y)
False
print(x ++ y)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(x ++ y)
TypeError: bad operand type for unary +: 'list'
print(x == y)
True
print(x is not z)
False
print(x is not y)
True
print(x=!y)
SyntaxError: invalid syntax
print(x!=y)
False
>>> x=["apple","banana"]
>>> print("banana" in x)
True
>>> x=["apple","banana"]
>>> print("pineapple" not in x)
True
>>> str1="welcome"
>>> str2="come"
>>> print(str2 in str1)
True
>>> str1="welcome"
>>> str2="go"
>>> print(str2 in str1)
False
>>> print("come not in str1")
come not in str1
>>> a=60
>>> b=13
>>> print("a:",a,"b:","a&b:",a&b)
a: 60 b: a&b: 12
>>> print(a&b)
12
>>> bin(a)
'0b111100'
>>> int("1100",2)
12
>>> bin(12)
'0b1100'
>>> a=10
>>> b=5
>>> print(a&b)
0
>>> bin(a&b)
'0b0'
>>> int("0000",2)
0
>>> a=60
>>> b=13
>>> print(a|b)
61
>>> bin(a|b)
'0b111101'
>>> int("111101",2)
61
>>> print(10^5)
15
>>> print(10~5)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(10~5)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=10
>>> ~a
-11
>>> bin(~a)
'-0b1011'
