
correct_word = "APPLE"

#Instructions
print("Welcome to WYRDLE!")
print("the Joshua Steele version")
print("A copy of the original Wordle game by Josh Wardle")

#Turns
total_guesses = 6

#Turn loop
for current_guess in range(total_guesses):
    guess = input(f"\n(Attempt {current_guess+1}) Guess a 5-letter word: ").upper()

    #Player WIN
    if guess == correct_word:
        print("\nYOU WON!!!")
        print("You found the word in ", current_guess+1, " attempts")
        break

    #Check lenth of word
    if len(guess) != 5:
        print(f"Your word has {len(guess)} letters!")
        print("Please enter a 5-letter word :)")
        continue

    correct_letters = 0
    misplaced_letters = 0
    wrong_letters = 0

    letters_to_check = list(correct_word) #list made up of letters of correct_word
    indexes_already_checked = []    #to save list of indexes of correct and misplaced letters 
                                    #so that loops only check once for each letter

    #Check correct letters
    for i in range(len(correct_word)):
        if guess[i] == correct_word[i]:
            letters_to_check.remove(guess[i]) 
            indexes_already_checked.append(i) 
            correct_letters += 1
    print("Correct letters: ", correct_letters)

    #Check misplaced letters
    for correct_letter, guess_letter in zip(correct_word, guess):
        if correct_letter == guess_letter:
            continue
        if guess_letter in letters_to_check:
            letters_to_check.remove(guess_letter)
            misplaced_letters += 1
    print("Misplaced letters: ", misplaced_letters)
    
    #Check wrong letters
    print("Wrong letters: ", len(letters_to_check))

    #Player LOSE
    if current_guess+1 >= total_guesses:
        print("\nYOU LOSE :(")
        print("You ran out of attempts")
        print("The word to find was: ", correct_word)