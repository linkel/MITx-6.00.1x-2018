# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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

def wasLetterGood(theletter, secretWord):
    '''
    theletter: char, the most recent letter guessed by user.
    secretWord: string, the secret word to guess.
    returns: boolean, whether the letter was in the word or not
    '''
    if theletter in secretWord:
      return True
    else:
      return False

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print('Welcome to the game Hangman!')

    print('I am thinking of a word that is ' + str(len(secretWord)) + " letters long")

    guesses = 8
    lettersGuessed = []
    theword = secretWord
    #mistakesMade = 0

    while guesses > 0:
      print('-----------')
      if isWordGuessed(theword, lettersGuessed) == True:
          print('Congratulations, you won!')
          break
      print('You have ' + str(guesses) + ' guesses left')
      print('Available Letters: ' + getAvailableLetters(lettersGuessed))
      guess = input("Please guess a letter: ")
      if guess in getAvailableLetters(lettersGuessed):
        lettersGuessed.append(guess)
        if wasLetterGood(guess, theword):
          print('Good guess: ' + str(getGuessedWord(theword, lettersGuessed)))
        else:
          print('Oops! That letter is not in my word: ' + str(getGuessedWord(theword, lettersGuessed)))
          guesses -= 1
      else:
        print('Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(theword, lettersGuessed)))
        
      
      
    if guesses == 0 and isWordGuessed(theword, lettersGuessed) == False:
      print('-----------')
      print('Sorry, you ran out of guesses. The word was ' + theword + '.')











# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
