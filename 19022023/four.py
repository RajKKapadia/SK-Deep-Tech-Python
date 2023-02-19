'''
MODULE
'''

from my_first_package.my_first_module import *

answer = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(answer)

from my_first_package.my_first_module import add

from my_first_package import my_first_module
my_first_module.add()