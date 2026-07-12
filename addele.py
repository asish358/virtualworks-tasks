Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=["apple","banana","cherry"]
>>> list1.append("orange")
>>> 
>>> print(list1)
['apple', 'banana', 'cherry', 'orange']
>>> list1=[1,2,3,4]
>>> sum=add(list1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sum=add(list1)
NameError: name 'add' is not defined
