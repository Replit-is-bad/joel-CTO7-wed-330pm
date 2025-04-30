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

with open('FiveLetterWords.csv','r') as fileobj :
    
    # reads and stores it into a string
    contents = fileobj.read()

    print(contents)

    # splilt words into items in a list
    wordlist = contents.split(",")
    
    wordle = random.choice(wordlist)

    