def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    origbase = base
    while exp > 1:
        base *= origbase
        exp -= 1
    if exp == 0:
        base = 1
    return base

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        base = 1
        return base
    elif exp == 1:
        return base
    else:
        return (base * (recurPower(base, exp - 1)))