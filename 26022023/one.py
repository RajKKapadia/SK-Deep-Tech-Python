'''
OOP
Class and Object
Class is a kind of a blueprint, from that blueprint, you can create object, and perform actions.
'''

# class className:
#     '''
#     Class body
#     '''
#     def __init__(self):
#         '''
#         Do the things to create an object of the class..
#         '''


class Animal:
    '''
    Animals have few common things:
        - they have number legs
        - they can be pet or not
        - they are wild or not
        - they have wings or not
    '''

    def __init__(self, name: str, legs: int, is_wild: bool) -> None:
        self.name = name
        self.legs = legs
        self.is_wild = is_wild

    def information(self) -> None:
        wild = ''
        if self.is_wild:
            wild += ' is a wild animal'
        else:
            wild += ' is not a wild animal'
        print(f'{self.name}{wild}, they have {self.legs} legs.')


# lion = Animal('Lion', 4, True)
# lion.information()

# peacock = Animal('Peacock', 2, False)
# peacock.information()

class Cars:
    '''
    Cars have common things
        - automatic or manual
        - petrol or diesel or electric
        - hatchback, sedan, suv, sports
        - Maker
        - Model
    '''

    def __init__(self, is_automatic: str, fuel_type: str, type: str, maker: str, model: str) -> None:
        self.is_automatic = is_automatic
        self.fuel_type = fuel_type
        self.type = type
        self.maker = maker
        self.model = model

    def information(self) -> None:
        '''
        Polo car is made by Vwokswagon, it runs on petrol, it has automatic gear system, and it is a Hatchback car.
        '''
        # automatic = ''
        # if self.is_automatic:
        #     automatic += 'automatic'
        # else:
        #     automatic += 'manual'
        
        print(f'''{self.model} car is made by {self.maker}, it runs on {self.fuel_type}, is has {self.is_automatic} gear system, and it is a {self.type} car.''')

polo = Cars('automatic', 'Diesel', 'Hacthcback', 'Vwokswagon', 'Polo')
# polo.information()
print(polo.is_automatic)

s3 = Cars('automatic', 'Electric', 'Sedan', 'Tesla', 'S3')
# s3.information()
