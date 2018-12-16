def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    totals = {}
    for letters in secretWord:
        if letters in lettersGuessed:
            totals[letters] = 1
        else:
            totals[letters] = 0
    if 0 in totals.values():
        return False
    else:
        return True
    

apple = 'apple'
speda = ['s', 'p', 'e', 'd', 'a']
bapple = ['a', 'p', 'p', 'l', 'e']

print(isWordGuessed(apple, bapple))