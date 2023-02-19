from typing import Any

def add(*values: Any) -> Any:
    '''
    This function adds all the values and return
    '''
    total = 0

    for v in values:
        total += v
    
    return total
