**Problem 1: Word scores**
The first step is to implement a function that calculates the score for a single word. 
Fill in the code for get_word_score in ps3.py according to the function specifications.
As a reminder, here are the rules for scoring a word: 
    - The score for a word is the product of two components: 
        - First component: the sum of the points for letters in the word. 
        - Second component: either [7 * word_length - 3 * ( n- word_length)] or 1, whichever value is greater, where: 
            - **word_length** is the number of letters used in the word 
            - **n** is the number of letters available in the current hand.

You should use the `SCRABBLE_LETTER_VALUES` dictionary defined at the top of ps3.py.
Do not assume that there are always 7 letters in a hand! 
The parameter n is the total number of letters in the hand when the word was entered. 
Finally, you may find the str.lower function helpful:s = “My string”print(s.lower())>>>> “my string”

If you don’t know what this does you could try typing help(str.lower) in your Spyder shell to see the documentation for the functions. 

Testing: If this function is implemented correctly, and you run test_ps3.py , the `test_get_word_score()` tests will pass. You should also test your implementation of `get_word_score` yourself, using some reasonable English words. 

**Note that the wildcard tests will crash due to a KeyError. This is fine for now - you will fix this in Problem 4.**