Hangman Game Requirements
You will implement a function called hangman that will allow the user to play hangman
against the computer. The computer picks the word, and the player tries to guess
letters in the word.

Here is the general behavior we want to implement. Don’t be intimidated! This is just
a description; we will break this down into steps and provide further
functional specs later on in the pset so keep reading!
1. The computer must select a word at random from the list of available words
that was provided in words.txt
Note that words.txt contains words in all lowercase letters.
2. The user is given a certain number of guesses at the beginning.
3. The game is interactive; the user inputs their guess and the computer either:
a. reveals the letter if it exists in the secret word
b. penalize the user and updates the number of guesses remaining
4. The game ends when either the user guesses the secret word, or the user runs
out of guesses.