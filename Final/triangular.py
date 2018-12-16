def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    # Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. 
    # For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

    kcopy = k
    intn = 1
    while kcopy - intn >= 0:
        if kcopy - intn == 0:
            return True
        else:
            kcopy -= intn
            intn += 1
    return False

print(is_triangular(105))