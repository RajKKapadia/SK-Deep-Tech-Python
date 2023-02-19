'''
TRY and CATCH
'''

def divide(a: int, b: int) -> float:

    try:
        '''
        We try to run this
        '''
        print(a/b)
    except:
        '''
        Something goes wrong
        '''
        print('Something went wrong.')
    else:
        '''
        If everything works well
        '''
        print('Everything worked.')
    finally:
        '''
        Irrespective of the code works or not
        '''
        print('This is finally.')

answer = divide(2, 0)
if answer != None:
    print(answer)
