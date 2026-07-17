Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(10>9)
True
print(10==9)
False
print(10<9)
False
print(bool("hello"))
True
print(bool(15))
True
x="hi"
y=10
print(bool(x))
True
print(bool(y))
True
bool("asish")
True
bool(123)
True
bool(["apple"],[cherry"],["banana"])
                
SyntaxError: unterminated string literal (detected at line 1)
bool(["apple","cherry","banana"])
                
True
bool(false)
                
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
bool(false)
                
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
bool(none)
...                 
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bool(none)
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> bool(0)
...                 
False
>>> bool("")
...                 
False
>>> bool(())
...                 
False
>>> bool([])
...                 
False
>>> bool({})
...                 
False
>>> bool(None)
...                 
False
>>>  x=5
...                 
SyntaxError: unexpected indent
>>> x=5
...                 
>>> y=8
...                 
>>> x+y
...                 
13
>>> x-y
...                 
-3
>>> x*y
...                 
40
>>> x/y
...                 
0.625
>>> x%y
...                 
5
>>> x**y
...                 
390625
>>> x//y
...                 
0
>>> x=5
...                 
>>> print(x)
...                 
5
