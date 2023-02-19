'''
FUNCTIONS
'''

'''
SYNTAX
def YOURFUNCTIONNAME():
    BODY OF THE FUNCTION
'''

# def my_first_function():
#     print('This is my first function.')

# my_first_function()

'''
Values in the function known as input arguments.
'''

# def my_print(value: str) -> None:
#     '''
#     This is a replica of print function
#     '''
#     print(value)

# my_print('Hello there...')

from typing import Any

def add(a: Any, b: Any) -> Any:
    '''
    The function adds two variables a and b.
    '''
    if type(a) == type(b):
        return a + b
    else:
        print('The variables are not the same type.')

answer = add('Hello', 'World')
print(answer)

answer = add(1, 2)
print(answer)

answer = add(1.6, 7)
print(answer)

answer = add([1, 2, 3], ['a', 'b', True, 3])
print(answer)

answer = add(5, 'Hello')
if answer != None:
    print(answer)
