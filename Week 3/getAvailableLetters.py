def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alletters = string.ascii_lowercase
    alletList = []
    enderList = []
    for letters in alletters:
        alletList.append(letters)
    for i in alletList:
        if i not in lettersGuessed:
            enderList.append(i)
    return ''.join(enderList)



apple = 'apple'
speda = ['s', 'p', 'e', 'd', 'a']
bapple = ['a', 'p', 'p', 'l', 'e']
bipple = ['u', 'z', 'y', 'e', 's', 'o', 'w', 'l', 'p', 'v', 'q']
tester = ['a', 'b', 'q', 'p', 't', 's']
print(getAvailableLetters(tester))