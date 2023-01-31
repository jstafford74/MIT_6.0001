# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "ps3/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word:str, n:int) -> int:
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_len = len(word)
    word = word.lower()
    first_component_score = 0
    second_component_score = max(1,7 * word_len - 3 * (n - word_len))
    
    if word_len == 0:
        return first_component_score
    # First component scoring
    else:
        for letter in word:
            letter_score = SCRABBLE_LETTER_VALUES[letter]
            
            first_component_score += letter_score
           
         
    return first_component_score * second_component_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    keys:list[str] = []
    for letter in hand.keys():
        keys.append(letter)      # print all on the same line
    # print()                              # print an empty line
    return " ".join(keys)
#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = 1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand:dict[str,int], word:str) -> dict[str, int]:
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    lower_word = word.lower()
    new_hand:dict[str,int] = hand.copy()
    
    for letter in lower_word:
        letter_freq = hand.get(letter,0)
        new_letter_freq = new_hand.get(letter,0)

        if letter_freq == 1:
            new_hand.pop(letter)
        if letter_freq > 1:
            if new_letter_freq - 1 == 0:
                new_hand.pop(letter)  
            else:
                new_hand[letter] = new_letter_freq - 1

    return new_hand
         
WORDLIST = load_words()         
#
# Problem #3: Test word validity
#
def is_valid_word(word:str, hand:dict[str,int], word_list:list[str]) -> bool:
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # Check if all letters in hand
    lower_word = word.lower()
    word_dict:dict[str,int] = get_frequency_dict(lower_word)
    hand_copy_dict:dict[str,int] | bool = hand.copy()
    poss_words:set[str] = {''}
    has_word:bool = False
    
    def starred_words(word:str) -> set[str] :       
        starred_words:set[str] = set()
        if '*' in word:
            starred_words.add(word)
            return starred_words
        for index,letter in enumerate(word):
            starred_word = list(word.lower())
            if letter.lower() in VOWELS:
                new_word = starred_word
                new_word[index] = "*"
                starred_words.add("".join(new_word))
            
        return starred_words
    
    for each_word in word_list:
        if len(each_word) == len(word):
            check_words = starred_words(each_word)
            starredWords = starred_words(word)
            has_word = True if len(check_words.intersection(starredWords)) > 0 else False
            if has_word == True:
                poss_words = check_words.intersection(starredWords)
                poss_words.add(word)
   
    has_word = True if word in list(poss_words) else False
    
    ## Iterate through the hand and compare letter frequency to the word letter frequency
    if has_word and len(hand.keys()) > 0:
        for letter in word_dict.keys():
            handFreq = hand.get(letter,0)
            wordFreq = word_dict.get(letter,0)
            #Player has the letter in hand
            if handFreq > 0:
            ## Player has exactly enough letters
               if handFreq == wordFreq:              
                hand_copy_dict.pop(letter)
            ## Player has more than enough letters
               if handFreq > wordFreq:
                hand_copy_dict[letter] = handFreq - wordFreq              
            ## Player does not have enough letters
               if handFreq < wordFreq:                
                hand_copy_dict = False
                break
            else:
                hand_copy_dict = False
                break
                   
        if type(hand_copy_dict) == dict: 
           hand_copy_dict = True
    else:
        hand_copy_dict = False                   
    
    return hand_copy_dict             


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand:dict[str,int]) -> int:
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """    
    hand_len:int = len(hand.keys())
    return hand_len

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    cur_hand = hand.copy()
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while len(cur_hand.keys()) > 0:
    # Display the hand
        displayHand = display_hand(cur_hand)
        print("Current Hand:",displayHand)
        
    # Ask user for input
        cur_word:str = input("Enter word, or '!!' to indicate that your are finished:")  
    # If the input is two exclamation points:
        if cur_word == '!!':
            print("Total score:",total_score,"points")
            break    
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(cur_word,cur_hand, word_list) is True:
                cur_score = get_word_score(cur_word,len(cur_hand.keys()))
                total_score += cur_score
                # Tell the user how many points the word earned,
                # and the updated total score
                print(f'"{cur_word}" earned {cur_score} points. Total: {total_score} points')
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            else:
                print("That is not a valid word. Please choose another word") 
               
            # update the user's hand by removing the letters of their inputted word
            cur_hand = update_hand(cur_hand,cur_word)
    
    if len(cur_hand.keys()) == 0:    
        print("Ran out of letters. Total score for this hand:",total_score)
    else:
        print("Total score for this hand:",total_score)
   
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    is_vowel = True if VOWELS.find(letter) > 0 else False
    is_consonant = True if CONSONANTS.find(letter) > 0 else False
    
    new_hand = hand.copy()
    if letter in new_hand.keys():
        freq = new_hand.get(letter)
        new_hand.pop(letter)
        if is_vowel:
          vowels = list(VOWELS)
          vowels.remove(letter)  
          new_vowel = random.choice(vowels)
          new_hand.update({new_vowel:freq})
        if is_consonant:
          consonants = list(CONSONANTS)
          consonants.remove(letter)  
          new_consonant = random.choice(consonants)
          new_hand.update({new_consonant:freq})
    else:
        return new_hand
    
    return new_hand  
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    series_score:int = 0
    HAND_SIZE = 7
    num_hands:int = int(input("Enter total number of hands:"))
    
        
    # if num_hands <= 0:
    #     print("Please enter a number greater than or equal to 1")
    #     num_hands:int = input("Enter total number of hands:")
    
    while num_hands > 0:
        cur_hand_score:int = 0
        hand = deal_hand(HAND_SIZE)
        print("hand:",hand)
        print("num hands:",num_hands)
        displayHand = display_hand(hand)
        print("Current Hand:",displayHand)
        wants_substitution = input("Would you like to substitute a letter?")
        
        if wants_substitution.lower() == 'yes':
            substitute_letter = input("Which letter would you like to replace:")
            hand = substitute_hand(hand,substitute_letter)
      
        cur_hand_score += play_hand(hand,word_list)
        print("------------")                        
        wants_replay = input("Would you like to replay the hand?")
       
        if wants_replay == 'yes':
            cur_hand_score = 0
            cur_hand_score += play_hand(hand,word_list)
            print("------------") 
            num_hands -= 1 
        else:
            num_hands -= 1
        series_score += cur_hand_score
    print("Total score over all hands:",series_score)       
  
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
