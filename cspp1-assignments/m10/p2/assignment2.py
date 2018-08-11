'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

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
    i = 0
    if lettersGuessed[i] in secretWord:
        return True
    else:
        return False
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s_str = ""
    for m_input in secretWord:
        if m_input not in lettersGuessed:
            s_str = s_str + "_"
        else:
            s_str = s_str+m_input
    return s_str


import string
ALPHA_BETS = string.ascii_lowercase
def getAvailableLetters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    answer = []
    for letter_given in ALPHA_BETS:
        if letter_given not in letters_guessed:
            answer.append(letter_given)
    return ''.join(answer)

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + "letters long.")
    guesschances = 8
    won = 0
    guessedletters = []
    while guesschances > 0 and won!= 1:
        print("----------------------------")
        print("available letters", getAvailableLetters(guessedletters))
        print("chances left", guesschances)
        l =list(input("guess a letter please: "))
        if l[0] in guessedletters:
            print("Oops! You have already guessed that letter:",getGuessedWord(secretWord, guessedletters))
        else:
            guessedletters = guessedletters + l
            if isWordGuessed(secretWord, l) == True:
                print("well guessed", getGuessedWord(secretWord, guessedletters))
                if secretWord == getGuessedWord(secretWord, guessedletters):
                    won = 1
            else:
                print("Oops! That letter is not in my word: ",getGuessedWord(secretWord, guessedletters))
                guesschances = guesschances - 1
    if won == 1:
        print("you won")
    else:
        print("Sorry, you ran out of guesses. The word was : ", secretWord)

    



def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    
    hangman(secretWord)


if __name__ == "__main__":
    main()
