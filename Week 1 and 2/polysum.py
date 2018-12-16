from math import *

def polysum(n, s):
    '''
    n: int or float
    s: int or float
    
    returns:int or float, sums area and square of the perimeter of the regular polygon
    '''
    # area of a regular polygon
    area = ((0.25)*n*s**2)/(tan(pi/n))
    # the perimeter of a regular polygon, squared
    sqperimeter = (n*s)**2
    # returning the value calculated -- the sum of the above variables
    return round((area + sqperimeter),4)