Problem 2
Hangman Part 1: Three helper functions
Before we have you write code to organize the hangman game, we are going to break
down the problem into logical subtasks, creating three helper functions you will need to have in order for this game to work. This is a common approach to computational problem solving, and one we want you to begin experiencing.

The file hangman.py has a number of already implemented functions you can use
while writing up your solution. You can ignore the code in the two functions at the top of the file that have already been implemented for you, though you should understand how to use each helper function by reading the docstrings.

1A) Determine whether the word has been guessed
First, implement the function is_word_guessed that takes in two parameters a
string, secret_word , and a list of letters (strings), letters_guessed. This function returns a boolean True if secret_word has been guessed (i.e., all the letters of secret_word are in letters_guessed ), and False otherwise. This function will be useful in helping you decide when the hangman game has been successfully completed, and becomes an endtest for any iterative loop that checks letters against the secret word.

For this function, you may assume that all the letters in secret_word and
letters_guessed are lowercase.

Example Usage:
>>> secret_word = 'apple'
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(is_word_guessed(secret_word, letters_guessed) )
False
1B) Getting the user’s guess
2
Next, implement the function get_guessed_word that takes in two parameters a
string, secret_word , and a list of letters, letters_guessed . This function returns a
string that is comprised of letters and underscores, based on what letters in
letters_guessed are in secret_word . This shouldn't be too different from
is_word_guessed !
We are going to use an underscore followed by a space (_ ) to represent unknown
letters. We could have chosen other symbols, but the combination of underscore and
space is visible and easily discerned. Note that the space is super important, as
otherwise it hard to distinguish whether ____ is four elements long or three. This is
called usability it's
very important, when programming, to consider the usability of
your program. If users find your program difficult to understand or operate, they
won't use it! We encourage you to think about usability when designing your program.
Hint: In designing your function, think about what information you want to return
when done, whether you need a place to store that information as you loop over a
data structure, and how you want to add information to your accumulated result.
Example Usage:
>>> secret_word = 'apple'
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(get_guessed_word(secret_word, letters_guessed) )
'_ pp_ e'
1C) Getting all available letters
Next, implement the function get_available_letters that takes in one parameter a
list of letters, letters_guessed . This function returns a string that is comprised of
lowercase English letters all
lowercase English letters that are not in
letters_guessed .
This function should return the letters in alphabetical order. For this function, you may
assume that all the letters in letters_guessed are lowercase.
Hint : You might consider using string.ascii_lowercase , which is a string comprised
of all lowercase letters:
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
Example Usage:
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print get_available_letters(letters_guessed)
abcdfghjlmnoqtuvwxyz
