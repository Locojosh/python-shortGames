#wyrdle.py 
import pathlib
import random
from string import ascii_letters, ascii_uppercase
from rich.console import Console 
console = Console(width=40)
from rich.theme import Theme

console = Console(width=40, theme = Theme({"warning":"red on yellow"}))

NUM_LETTERS = 5
NUM_GUESSES = 6
WORDS_PATH = pathlib.Path(__file__).parent / "wordlist.txt"

def main():
    #Pre-Process
    correct_word = get_random_word(WORDS_PATH.read_text(encoding="utf-8").split("\n"))
    print(correct_word) #********comment this line for final game version
    guesses = ["_____"*NUM_LETTERS]*NUM_GUESSES #create empty list

    #Process (main loop)
    show_game_instructions()

    for nGuess in range(NUM_GUESSES):
        refresh_page(headline=f"Guess {nGuess+1}")

        #Show correct, misplaced and incorrect letters of the word guessed
        #show_word_guessed(guesses[nGuess], correct_word)
        show_gueses(guesses, correct_word)

        guesses[nGuess] = guess_word(previous_guesses= guesses[:nGuess])

        #Check for CORRECT answer
        if guesses[nGuess] == correct_word:
            break
        
    #Post-Process
    game_over(guesses, correct_word, guessed_correctly=guesses[nGuess]==correct_word)


def get_random_word(word_list):
    """Get a random five-letter word from a list of strings.

    ## Example:
    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    """

    if words := [
        word.upper()
        for word in word_list
        if len(word) == NUM_LETTERS and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)
    else:
        console.print(f"No words of length {NUM_LETTERS} in the word list", style="warning")
        raise SystemExit()
        
def show_game_instructions():
    print("Welcome to WYRDLE!")
    print("the Joshua Steele version")
    print("A copy of the original Wordle game by Josh Wardle")

def guess_word(previous_guesses):
    guess = console.input(f"\nGuess a {NUM_LETTERS}-letter word: ").upper()

    if guess in previous_guesses:
        console.print(f"You have already guessed the word '{guess}'", style = "warning")
        return guess_word(previous_guesses)

    if len(guess) != NUM_LETTERS:
        console.print(f"Your word must be {NUM_LETTERS} letters long!", style="warning")
        return guess_word(previous_guesses)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(f"Invalid letter: '{invalid}'. Please use English letters :)", style="warning")
        return guess_word(previous_guesses)

    return guess

#Not currently used (used in previous version)
def show_word_guessed(guess, correct_word):
    """Show the user's guess on the terminal and classify all letters.
    ## Example:
    >>> show_word_guessed("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """

    correct_letters = {
        letter for letter, correct_letter in zip(guess, correct_word) if letter == correct_letter
    }
    misplaced_letters = set(guess) & set(correct_word) - correct_letters
    wrong_letters = set(guess) - set(correct_word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

def show_gueses(guesses, correct_word):
    letters_in_alphabet = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, correct_word):
            if letter == correct:
                style = "bold white on green"
            elif letter in correct_word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                letters_in_alphabet[letter] = f"[{style}]{letter}[/]"
        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letters_in_alphabet.values()), justify="center")

def game_over(guesses, correct_word, guessed_correctly):
    #print("\nYOU LOSE :(")
    #print("You ran out of attempts")
    #print("The word to find was: ", correct_word)
    #print(f"The word to find was: {correct_word}")
    refresh_page(headline="YOU WON!!!" if guessed_correctly else "Game Over :(")
    show_gueses(guesses, correct_word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {correct_word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {correct_word}[/]")

def refresh_page(headline):
    console.clear()
    console.rule(f":leafy_green: {headline} :leafy_green:")


if __name__ == "__main__":
    main()