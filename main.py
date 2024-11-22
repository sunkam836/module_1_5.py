immutable_var = 35, 15, 'keep', 'highway'
print(immutable_var)
print(type(immutable_var))
# immutable_var [0] = 73 - Traceback (most recent call last):
# File "D:\PycharmProjects\module_1_5.py\main.py", line 8, in <module>
# immutable_var [0] = 73
#TypeError: 'tuple' object does not support item assignment
mutable_var = [54,37,65],365
print(mutable_var)
mutable_var [0][0] = 'sea'
print(mutable_var)
