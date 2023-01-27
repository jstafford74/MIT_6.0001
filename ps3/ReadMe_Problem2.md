## Problem 2:

# Dealing with Hands

## Representing Hands
 A hand is the set of letters held by a player during the game. The player is initially dealt
 a set of random letters. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`.
 In our program, a hand will be represented as a **dictionary:** the keys are (lowercase) letters and the values are
 the number of times the particular letter is repeated in that hand. For example, the above hand would be represented
 as: `hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}`. 
 
 Notice how the repeated letter 'l' is represented.  With a dictionary representation, the usual way to access a value is hand['a'], where 'a' is the key we want to find.
 
 However,this only works if the key is in the dictionary; otherwise, we get a `KeyError`. To avoid this, we can instead
 use the function call `hand.get('a',0)`. This is the "safe" way to access a value if we are not sure the key is in
 the dictionary. `d.get(key,default)` returns the value for key if key is in the dictionary `d` , else it returns
 default . If default is not given, it returns `None` , so that this method never raises a `KeyError`. 
 
## Converting Words Into Dictionary Representation
 One useful function we've defined for you is `get_frequency_dict`, defined near the top of ps3.py. When given a
 string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of
 times that letter is represented in the input string.

For example: 
```python
    >> get_frequency_dict("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
  As you can see, this is the same kind of dictionary we use to represent hands. 
    
## Displaying a Hand
 Given a hand represented as a dictionary, we want to display it in a user-friendly way. We have provided the
 implementation for this in the `display_hand` function. 
 
## Generating a Random Hand
 The hand a player is dealt is a set of letters chosen at random. We provide you with a function that generates a random hand, `deal_hand`. The function takes as input a positive integer `n`, and returns a new dictionary representing a hand of n lowercase letters. 
 
## Removing Letters From a Hand
 The player starts with a full hand of n letters. As the player spells out words, letters from the set are used up.
 For example, the player could start with the following hand: `a, q, l, m, u, i, l`. The player could choose to play
 the word quail. This would leave the following letters in the player's hand: l, m. You will now write a function that
 takes a *hand* and a *word* as inputs, uses letters from that hand to spell the word, and returns a new hand
 containing only the remaining letters. Your function should not modify the input hand.

For example: 
```python
    >> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    >> display_hand(hand) 
    a q l l m u i
    >> new_hand = update_hand(hand, 'quail')
    >> new_hand
    {'l': 1, 'm': 1}
    >> display_hand(new_hand)
    l m
    >> display_hand(hand)
    a q l l m u i
```   
  (**NOTE:** Alternatively, in the above example, after the call to `update_hand` the value of `new_hand` could be the dictionary `{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}` . The exact value depends on your implementation; but the output of `display_hand()` should be the same in either case.)
  
  **IMPORTANT:** If the player guesses a word that is invalid, either because it is not a real word or because they used letters that they don't actually have in their hand, they still lose the letters from their hand that they did guess as a penalty. Make sure that your implementation accounts for this! Do not assume that the word you are given only uses letters that actually exist in the hand. 

For example:
```python
    >> hand = {'j':2, 'o':1, 'l':1, 'w':1, 'n':2}
    >> display_hand(hand)
    j j o l w n n
    >> hand = update_hand(hand, 'jolly')
    >> hand
    {'j': 1, 'w': 1, 'n': 2} 
    >> display_hand(hand)
    j w n n
```
Note that one 'j', one 'o', and one 'l' (despite that facts that the player tried to use two, because only one existed
in the hand) were used up. The 'y' guess has no effect on the hand, because 'y' was not in the hand to begin with.
Also, the same note from above about alternate representations of the hand applies here. 

Implement the `update_hand` function according to the specifications in the skeleton code. 
**HINT:** You may wish to review the documentation for the " .copy " method of Pythondictionaries.

**Testing:** Make sure the `test_update_hand` tests pass. You may also want to test your implementation of `update_hand` with some reasonable inputs.