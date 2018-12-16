def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    import math
    determine = num
    count = 0
    while determine > base:
        determine = determine/base
        count += 1
    #print(count)
    guess = round(count, 0)
    while True:
        test = base**guess
        if test > num:
            below = base**(guess-1)
            if test - num < num - below:
                return guess
            elif test - num >= num - below:
                return guess-1
        if test < num:
            above = base**(guess+1)
            if above - num < num - test:
                return guess+1
            if above - num >= num - test:
                return guess
        if test == num:
            return guess

print(closest_power(4, 1))