'''
A problem where I dont know how many times I need to repeat this...
'''
# for i in range(5):
#     print(i)

'''
WHILE
'''
# while condition:
#     '''
#     ALL THE CODE
#     '''

'''
BREAK
CONTINUE
'''

# index = 0

# while index < 5:
#     print(f'I am in the while loop, index {index}')
#     index += 1 # index = index + 1
#     if index == 2:
#         continue

'''
Print the sum of all the numbers that the user enters
And also print all the numbers as well...
'''

numb = int(input('Enter a number: '))

total = numb
all_numbers = []
all_numbers.append(numb)

while numb != 0:
    numb = int(input('Enter a number: '))
    total += numb
    if numb != 0:
        all_numbers.append(numb)

print(f'The sum is {total}.')
print('All the numbers: ')
print(all_numbers)
