low = 0
high = 100
userin = 0
print("Please think of a number between 0 and 100!")
while True:
    guess = (high + low)//2
    print("Is your secret number " + str(guess) + "?")
    userin = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if userin == 'h':
        high = guess
    if userin == 'l':
        low = guess
    if userin == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    if userin != 'h' and userin != 'l' and userin != 'c':
        print('Sorry, I did not understand your input.')
    