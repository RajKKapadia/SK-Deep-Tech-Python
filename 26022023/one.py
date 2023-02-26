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

lion = Animal('Lion', 4, True)
lion.information()

peacock = Animal('Peacock', 2, False)
peacock.information()

class Cars:
    '''
    Cars have common things
        - automatic or manual
        - petrol or diesel or electric
        - hatchback, sedan, suv, sports
        - Maker
        - Model
    '''