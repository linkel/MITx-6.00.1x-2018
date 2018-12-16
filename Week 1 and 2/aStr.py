def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle = (len(aStr)-1)//2
    
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return char == aStr
    else:
        guess = aStr[middle]
        if guess < char:
            aStr = aStr[middle+1:]
            if isIn(char, aStr):
                return True
            else:
                return False
        if guess > char:
            aStr = aStr[0:middle]
            if isIn(char, aStr):
                return True
            else:
                return False
        if guess == char:
            return True

#this version implements the middle+1: on the index, which makes it work and I don't need an extra case for len(aStr) == 2

yes = isIn("b","aaaccccccd")
print(str(yes))