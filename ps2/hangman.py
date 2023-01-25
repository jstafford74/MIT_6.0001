# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "ps2/words.txt"

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
secret_word = choose_word(wordlist)
## Original working program ##
# num_guesses = 10
# guess_num = 0
# letters_guessed = "_ " * len(secret_word)
# new_list = letters_guessed.split()
# letterz_guessed = []

# print("You have",num_guesses,"guesses. Good luck!")
# print("The secret word has",len(secret_word),"letters.")

# while letters_guessed != secret_word and guess_num < num_guesses:
#   print("Secret word:",letters_guessed)
#   print(num_guesses-guess_num,"remaining")
#   cur_guess = input("Please enter your guess: ")
#   guess_num += 1
#   if cur_guess in new_list:
#     print("You have already guessed that letter. Try again.")
#     guess_num -= 1
#     print("You still have",num_guesses-guess_num,"remaining")
    
#   if cur_guess in secret_word:
#     for index,letter in enumerate(secret_word):  
#       if letter == cur_guess: 
#         new_list[index] = cur_guess
#         letters_guessed = "".join(new_list)

# if letters_guessed != secret_word:
#   print("Sorry, you lose! The word was:",secret_word)
# if letters_guessed == secret_word:
#   print("You win! The word was:",secret_word)



def is_word_guessed(secret_word:str, letterz_guessed:list[str]) -> bool:
 new_list:list[str]|str = "_ " * len(secret_word)
 new_list = new_list.split()
 
 for guess in letterz_guessed:
  for index,letter in enumerate(secret_word):
    if letter == guess:
     new_list[index] = guess
 
 ret_val:str = "".join(new_list)
 if ret_val == secret_word:
   return True
 else:
   return False


def get_guessed_word(secret_word:str, letters_guessed:list[str]) -> str:
 new_list = "_ " * len(secret_word)
 new_list = new_list.split()

 for guess in letters_guessed:
   for index,letter in enumerate(secret_word):
    if letter == guess:
      new_list[index] = guess
 
 ret_val:str = " ".join(new_list)
 if ret_val == secret_word:
   ret_val = "".join(new_list)
     
 return ret_val



def get_available_letters(letters_guessed:list[str]) -> str:
  all_letters = list(string.ascii_lowercase)
  
  for letter in letters_guessed:
    for index,char in enumerate(all_letters):
      if char == letter:
        all_letters.pop(index) 
  
  return "".join(all_letters)
      

def hangman(secret_word:str):
    ## Starts up an interactive game of Hangman.
    ## Constants
    num_guesses = int(6)
    warnings = int(3)
    total_score = num_guesses
    letterz_guessed:list[str] = list()
    current_word = get_guessed_word(secret_word,letterz_guessed)
    available_letters = get_available_letters(letterz_guessed)
    vowels = ["a","e","i","o","u"]
    consonants = get_available_letters(vowels)
    ## At the start of the game, let the user know how many 
    ## letters the secret_word contains and how many guesses s/he starts with.
    ## This code runs once at start up.
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print(current_word)
    
    while is_word_guessed(secret_word,letterz_guessed) == False:
      print(secret_word)
      print("You have",warnings,"warnings left.")
      print("You have",num_guesses,"guesses left.")
      print("Remaining letters:",available_letters)
      cur_guess:str = input("Please guess a letter: ")
      
      ## Check if a letter, and only append to the list if it is a letter
      if cur_guess.isalpha():
        ## Check if the letter has been guessed
        if cur_guess in letterz_guessed:
          if warnings == 0:
            print("You lost a guess. Maximum warnings reached")
            num_guesses -= 1
          else:
            warnings -= 1
            print("WARNING! You have already guessed that letter.",warnings,"left.")
        ## If the letter has not been guessed yet..
        else:
          ## Append list if letter is alpha and not guessed yet
          letterz_guessed.append(cur_guess.lower())
          ## recalc available letters & the current word
          available_letters = get_available_letters(letterz_guessed)
          current_word = get_guessed_word(secret_word,letterz_guessed)
          ## Check if it is in the secret word
          if cur_guess in secret_word: 
            print("Good guess:",current_word) 
           
          ## If it hasn't been guessed and the letter is not in the secret word, penalize user
          else:
            if cur_guess in consonants:
              num_guesses -= 1
              print("Oops! You lost a guess:",current_word)
            if cur_guess in vowels:
              num_guesses -= 2
              print("Oops! You lost 2 guesses:",current_word)
      
      ## If maximum guesses reached, break the loop
      if num_guesses == 0:
        break
      
      ## If user guesses the correct word, break the loop
      if is_word_guessed(secret_word,letterz_guessed):
        break
   
    if is_word_guessed(secret_word,letterz_guessed):
        print("You win! The word was:",secret_word)
        

    else:
      print("Sorry, you lose! The word was:",secret_word)
       
hangman(secret_word)



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
