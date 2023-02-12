a = 25

# print(f'{a} x 1 = {a}')
# print(f'{a} x 2 = {a*2}')
# print(f'{a} x 3 = {a*3}')
# print(f'{a} x 4 = {a*4}')
# print(f'{a} x 5 = {a*5}')

'''
Scope of variable
'''

# for var in range(1, 11):
#     print(f'{a} x {var} = {a*var}')
#     print('something')
#     '''
#     perform some other tasks
#     '''


# a = ['a', 'b', 'c', 'd', 'e', 'f', True, ['1, 2, 3']]

# for c in a:
#     print(c)

# d = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }

# for k, v in d.items():
#     print(k, v)


'''
Print all the numbers divisible by 5 upto 20
'''

# for i in range(1, 31):

#     if i % 5 == 0:
#         print(i)

# '''
# Sum all the numbers upto 10
# '''

# sum = 0

# for i in range(11):
#     print(f'Index: {i}')
#     print(f'Sum: {sum}')
#     sum += i
#     print(f'After addition the Sum: {sum}')


# '''
# For loop inside a for loop
# NESTED FOR LOOP
# '''

# for i in range(5):
#     print('Outer loop...')
#     print(f'The index value is: {i}')

#     for j in range(2):
#         print('Inner loop...')
#         print(f'The index value is: {j}')


# '''
# Write a program to print table of a number given by the user.
# '''

# a = int(input('Enter a number: '))

# for i in range(1, 11):
#     print(f'{a} X {i} = {a * i}')


'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

# for row in range(1, 6):
#     for col in range(row):
#         print(row, end=' ')
#     print('')

'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''

# for row in range(1, 6):
#     for col in range(6, row, -1):
#         print(row, end=' ')
#     print('')

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

for row in range(1, 6):
    for col in range(6-row, 0, -1):
        print(col, end=' ')
    print('')

'''
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
'''