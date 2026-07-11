Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list=[1,2,3,4]
sumofnum=sum(list)
print(sumofnum)
10
average=sumofnum/len(list)
print(average)
2.5
max=max(list)
min=min(list)
print(max)
4
print(min)
1
>>> element=4
>>> count=list.count(element)
>>> print(count)
1
>>> list=[1,2,3,1,,2,1,3,1]
SyntaxError: invalid syntax
>>> list=[1,2,3,1,2,1,3,1]
>>> element=1
>>> count=list.count(element)
>>> print(count)
4
>>> list=["apple","banana","apple","cherry","apple"]
>>> list1=list(set(list))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list1=list(set(list))
TypeError: 'list' object is not callable
>>> list1=["apple","banana","apple","cherry","apple"]
>>> list2=list(set(list1))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list2=list(set(list1))
TypeError: 'list' object is not callable
>>> list1=["apple","banana","apple","cherry","apple"]
>>> list2 = list(set(list1))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list2 = list(set(list1))
TypeError: 'list' object is not callable
>>> list1=[1,2,2,3,4,4,5]
>>> list2= list(set(list1))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list2= list(set(list1))
TypeError: 'list' object is not callable
>>> lst = [1, 2, 2, 3, 4, 4, 5]
... unique_lst = list(set(lst))
... print("List after removing duplicates:", unique_lst)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> lst = [1, 2, 2, 3, 4, 4, 5]
... 
... unique_lst = list(set(lst))
... 
... print("List after removing duplicates:", unique_lst)
SyntaxError: multiple statements found while compiling a single statement
