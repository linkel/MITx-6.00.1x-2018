def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    tryn = 10
    if a > b:
        tryn = b
        print(tryn)
    elif b >= a:
        tryn = a
        print(tryn)
    while tryn > 0:
        testa = a % tryn
        testb = b % tryn
        print(testa)
        print(testb)
        if (testa == 0) and (testb == 0):
            break
        tryn = tryn - 1
        print(tryn)
    return tryn

example = gcdIter(81, 18)
print(example)