# Problem Set 2, hangman.py
# Name: Ellie
# Time spent: 2:30 - 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/Users/Ellie/Documents/code/MIT-Course/contents/assignments/ps2/words.txt"

def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    
    for c in secret_word:
        if c in letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    else:
        return False

# is_word_guessed('apple', ['e','i','p','l','s']) // False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    underscores = '_ '*len(secret_word)
    display = underscores.split()
    
    for c in secret_word:
        if c in letters_guessed:
            temp_indexes = [ i for i in range(len(secret_word)) if secret_word[i] == c ]
            for i in temp_indexes:
                display[i] = c
    return ' '.join(display)

# get_guessed_word('appletree',['e', 'i', 'k', 'p', 'r', 's']) // '_ p p _ e _ r e e'



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)

    for c in letters_guessed:
        if c in available_letters:
            i = available_letters.index(c)
            del(available_letters[i])
    return ''.join(available_letters)
        
# get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) // 'abcdfghjlmnoqtuvwxyz'
    
def is_valid_input(user_guess):
    '''
    user_guess: str, user's input
    reutrns: True or False if the input is a valid guess (alphabet letters only)
    '''
    letters = list(string.ascii_lowercase)
    
    if user_guess.lower() in letters:
        return True
    else:
        return False

# is_valid_input('A') // False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he/they starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he/they has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses = 6

    letters_guessed = []
    available_letters = string.ascii_lowercase
    won = False
    
    # iterate while the user still has guesses and has not won the game
    while guesses > 0 and not won:
        # prints welcome messages at the beginning of the game
        if len(letters_guessed) == 0:
            print('Welcome to the game of Hangman!')
            print('I am thinking of a word that is',len(secret_word),'letters long')
            print('_ '*len(secret_word))      
            print('You have', warnings,'warnings left')
        
        # informs users of how many guesses they have left, available letters, and asks for user to guess a letter
        print('You have', guesses,'guesses left')
        print('Available letters:',available_letters)
        print('Letters guessed:',','.join(letters_guessed))
        user_guess = input('Please guess a letter: ')
        
        # if the user's guess is a valid input, proceed with game
        if is_valid_input(user_guess):
            # if the user's has already guessed the letter, deduct 1 from their warnings or guesses if no warnings left
            if user_guess in letters_guessed:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses -= 1
                print('You already guessed that letter! You have',warnings,'warnings left')
            # if the user has not guessed the letter already
            else:
                letters_guessed.append(user_guess)
                available_letters = get_available_letters(letters_guessed)
                display_word = get_guessed_word(secret_word,letters_guessed)    
                
                # if user guesses wrong, deduct 1 from their guesses
                if user_guess not in secret_word:
                    guesses -= 1
                    print('Oops!',user_guess,'is not in my word.')
                else:
                    print('Great guess!',user_guess,'is in my word')   
                
                # checks if the user has guessed the secret word. if yes, change won to True to break out of the loop
                check_word = is_word_guessed(secret_word, letters_guessed)
                if check_word:
                    won = True
                    print('Congratulations! You won! You guessed the secret word!')
                print(display_word)
        # if the user's guess is not a valid input, deduct 1 from their warnings or guesses if no warnings left
        else:
            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1
            print('Please enter a valid guess! You have',warnings,'warnings left')

    # display to the user that they've lost and reveal the secret word        
    if guesses == 0:
        print('Sorry, you ran out of guesses! Better luck next time. The word was',secret_word)
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    x = my_word.replace(' ','')
    y = list(other_word)
    
    guessed_letters = []
    not_guessed_indexes = []
    
    # if length of my word and other word are not the same length, return False
    if len(other_word) != len(x):
        return False
    
    # for every guessed letter, append the letter to guessed_letters
    # for every letter not guessed, append the index to not_guessed_indexes
    for i in range(len(x)):
        if x[i] == '_':
            not_guessed_indexes.append(i)
        else:
             guessed_letters.append(x[i])
    
    # loop through not_guessed_indexes to check if missing letters in other_word were already guessed in my_word, return False
    for i in range(len(not_guessed_indexes)):
        if y[not_guessed_indexes[i]] in guessed_letters:
            return False
        
        # if missing letters were not already guessed, change them to _ and compare if the actual letters of my_word match with the corresponding letters of other_word
        y[not_guessed_indexes[i]] = '_'
        temp = ''.join(y)
        if temp == x:
            return True
        
    
# match_with_gaps('a_ pl_ ', 'ample') // True 
# match_with_gaps('a_ pl_ ', 'apple') // False 
    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    words = []
    
    for w in wordlist:
        if match_with_gaps(my_word, w):
            words.append(w)
    
    if len(words) == 0:
        return 'No matches found'

    return ' '.join(words)

# show_possible_matches('t_ _ t') // 'tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit'

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he/they starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he/they has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses = 6

    letters_guessed = []
    available_letters = string.ascii_lowercase
    display_word = get_guessed_word(secret_word,letters_guessed) 
    won = False
    
    # iterate while the user still has guesses and has not won the game
    while guesses > 0 and not won:
        # prints welcome messages at the beginning of the game
        if len(letters_guessed) == 0:
            print('Welcome to the game of Hangman!')
            print('I am thinking of a word that is',len(secret_word),'letters long')
            print('_ '*len(secret_word))      
            print('You have', warnings,'warnings left')
        
        # informs users of how many guesses they have left, available letters, and asks for user to guess a letter
        print('You have', guesses,'guesses left')
        print('Available letters:',available_letters)
        print('Letters guessed:',','.join(letters_guessed))
        user_guess = input('Please guess a letter: ')
        
        # if user enters special character to receive hints, display all possible matches without penalizing them for guess
        if user_guess == '*':
                print('Possible word matches are:',show_possible_matches(display_word))
        else:
            # if the user's guess is a valid input, proceed with game
            if is_valid_input(user_guess):
                # if the user's has already guessed the letter, deduct 1 from their warnings or guesses if no warnings left
                if user_guess in letters_guessed:
                    if warnings > 0:
                        warnings -= 1
                    else:
                        guesses -= 1
                    print('You already guessed that letter! You have',warnings,'warnings left')
                # if the user has not guessed the letter already
                else:
                    letters_guessed.append(user_guess)
                    available_letters = get_available_letters(letters_guessed)
                    display_word = get_guessed_word(secret_word,letters_guessed) 
                    
                    # if user guesses wrong, deduct 1 from their guesses
                    if user_guess not in secret_word:
                        guesses -= 1
                        print('Oops!',user_guess,'is not in my word.')
                    else:
                        print('Great guess!',user_guess,'is in my word')   
                    
                    # checks if the user has guessed the secret word. if yes, change won to True to break out of the loop
                    check_word = is_word_guessed(secret_word, letters_guessed)
                    if check_word:
                        won = True
                        print('Congratulations! You won! You guessed the secret word!')
                    print(display_word)
            # if the user's guess is not a valid input, deduct 1 from their warnings or guesses if no warnings left
            else:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses -= 1
                print('Please enter a valid guess! You have',warnings,'warnings left')

    # display to the user that they've lost and reveal the secret word        
    if guesses == 0:
        print('Sorry, you ran out of guesses! Better luck next time. The word was',secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
