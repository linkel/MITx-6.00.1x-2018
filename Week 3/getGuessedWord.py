def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    totals = {}
    wordHolder = []
    for letters in secretWord:
        if letters in lettersGuessed:
            totals[letters] = 1
        else:
            totals[letters] = 0
    for i in secretWord:
        if totals[i] == 0:
            wordHolder.append('_ ')
        if totals[i] == 1:
            wordHolder.append(i)
    return ''.join(wordHolder)
    

apple = 'apple'
speda = ['s', 'p', 'e', 'd', 'a']
bapple = ['a', 'p', 'p', 'l', 'e']

print(getGuessedWord(apple, speda))