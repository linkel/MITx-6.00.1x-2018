def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

    counter = 0
    secondcounter = -1
    while counter != secondcounter:
        for strings in L:
            if f(strings) == False:
                L.remove(strings)
                counter += 1
        secondcounter = counter
        for strings in L:
            if f(strings) == False:
                L.remove(strings)
                counter += 1
        
    return len(L)
    



#run_satisfiesF(L, satisfiesF)


def f(s):
    return 'a' in s
      
L = ['b', 'b', 'b', 'a', 'b', 'a']
print(satisfiesF(L))
print(L)
