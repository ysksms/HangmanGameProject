import random


def load_words(file_path):
    """
    Load a list of words from the given file and return them as a list.
    Each word should be on a new line in the file.
    """
    with open(file_path, "r") as file:
        return [word.strip() for word in file.readlines()]


def choose_random_word(words):
    """
    Select and return a random word from the list of words.
    """
    return random.choice(words)


def display_word_state(word, guessed_letters):
    """
    Display the word with underscores for unguessed letters and reveal
    correctly guessed letters.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def is_guess_valid(guess, guessed_letters):
    """
    Check if the guess is valid and return True if valid, else return False with a message.
    """
    if len(guess) != 1 or not guess.isalpha():
        return False, "---- Please enter a valid single letter. ----"
    if guess in guessed_letters:
        return False, f"---- You already guessed '{guess}'. Try another letter. ----"
    return True, None


def process_guess(guess, guessed_letters, word):
    """
    Process the player's guess and return the result and message.
    """
    if guess in word:
        guessed_letters.add(guess)
        return "correct", f"---- Good job! '{guess}' is in the word. ****"
    else:
        guessed_letters.add(guess)
        return "incorrect", f"---- Sorry, '{guess}' is not in the word. ----"


def check_game_over(word, guessed_letters, remaining_attempts):
    """
    Check if the game is over (win or lose) and return True if it is.
    """
    if remaining_attempts == 0:
        print(f"\n---- Game over! The word was: {word} ----")
        return True
    elif all(letter in guessed_letters for letter in word):
        print(f"\n**** Congratulations! You guessed the word: {word} ****")
        return True
    return False


def hangman_game(word):
    """
    Main game loop for the Hangman game.
    Manages the game flow, receiving the word to guess as input.
    """
    guessed_letters = set()
    remaining_attempts = 6

    print("**** Welcome to Hangman! ****")
    print("Try to guess the word!")

    while remaining_attempts > 0:
        # Display the current word state
        current_state = display_word_state(word, guessed_letters)
        print(f"\n* Current word: {current_state}")
        print(
            f"* Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}"
        )
        print(f"* Incorrect guesses remaining: {remaining_attempts}")

        # Get and validate the player's guess
        guess = input("* Guess a letter: ").lower()
        valid, message = is_guess_valid(guess, guessed_letters)
        if not valid:
            print(message)
            continue

        # Process the player's guess
        result, result_message = process_guess(guess, guessed_letters, word)
        print(result_message)

        if result == "incorrect":
            remaining_attempts -= 1

        # Check if the game is over
        if check_game_over(word, guessed_letters, remaining_attempts):
            break
