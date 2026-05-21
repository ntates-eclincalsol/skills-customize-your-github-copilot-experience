
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, and user input. Practice string manipulation, control flow, and handling user I/O.

## 📝 Tasks

### 🛠️	Build the Hangman Game

#### Description
Implement a terminal Hangman game that randomly selects a secret word from a predefined list and lets the player guess letters until they either reveal the whole word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Accept single-letter guesses (case-insensitive) and ignore repeated guesses.
- Display current progress in `_ _ _` format with correctly guessed letters revealed.
- Track and display the number of incorrect guesses remaining.
- End the game when the word is fully guessed (win) or attempts are exhausted (lose).
- Display a clear win or lose message including the final word.

#### Example Playthrough
```
Secret word: _ _ _ _ _ _
Guess a letter: p
Progress: P _ _ _ _ _
Incorrect guesses remaining: 6
Guess a letter: y
Progress: P Y _ _ _ _
...
You win! The word was PYTHON
```
