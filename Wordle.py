'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In this assignment, your task is to create a program that works like wordle. Your program will:

1. Choose a random word from the list

2. Allow you to input a 5-letter word

3. Validate if you have you have the letter in the correct position, correct letter but in the wrong position, or the wrong letter.

4. You can use the console output to print out the statements
'''
import random

def getword(wordlist):

    while True:
        guess = input('Guess the 5 letter word !')
        if len(guess) == 5:
            if guess.isalpha():
                if guess in wordlist:
                    return guess.upper()
                    pass
                else:
                    print('Yo momma is so fat when she got on the scale it said, "I need your weight not your phone number."')
            else:
                print('Yo mamma is so ugly when she tried to join an ugly contest they said, "Sorry, no professionals."')
        else:
            print('Yo momma so fat and old when God said, Let there be light, he asked your mother to move out of the way.')

with open('FiveLetterWords.csv','r') as fileobj :
    
    # reads and stores it into a string
    contents = fileobj.read()

    print(contents)

    # splilt words into items in a list
    wordlist = contents.split(",")
    
    wordle = random.choice(wordlist).upper()

for chance in range(1,7):
    checkguess = getword(wordlist)
    print(checkguess)
    display_check ='' 

    for i in range(len(wordle)):
        if checkguess[i] == wordle[i]:

            display_check = display_check + checkguess[i]

        elif checkguess[i]in wordle:
            display_check = display_check + '?'
            
        else:
            display_check = display_check + '#'

    print('')
    print(f'Attempt # : {chance}')
    print(f'You guess : {checkguess}')
    print(f'Result    : {display_check}')

    if checkguess == wordle:
        print('You are right!')
        print(f'{checkguess} is the answer!')
else:
    print('')
    print(f'THe actual word was {wordle}')