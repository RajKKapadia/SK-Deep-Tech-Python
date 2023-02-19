'''
More things about a function
How to pass multiple input arguments.
Different ways to pass the arguments.
'''

# def add(a, b, c, d):
#     return a + b + c + d

# answer = add(2, 3, 4, 5, 6)
# print(answer)

# def add(*values):
#     print(type(values))
#     print(values)
#     total = 0
#     for v in values:
#         total += v
    
#     return total

# answer = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(answer)

# d = {
#     'key_one': 'value one',
#     'key_two': 'value two',
#     'key_three': 'value three'
# }

# print(type(d))
# print(d)
# print(d.items())

# for k, v in d.items():
#     print(k, v)

keys = ['name', 'city', 'age', 'weight']

def my_print_function(**data):
    print(type(data))
    print(data)

    for key in data.keys():
        if key not in keys:
            return f'Unknow key {key}.'

    return f'You are {data["name"]} and you live in {data["city"]}.'

answer = my_print_function(name='Rajesh', cigty='Ahmedabad', age=34, weight=98)
print(answer)
