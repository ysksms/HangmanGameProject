import random


def load_words(file_path):
    """
    Load a list of words from the given file and return them as a list.
    Each word should be on a new line in the file.
    """
    with open(file_path, "r") as file:
        return [word.strip() for word in file.readlines()]


def choose_random_word(words, difficulty):
    """
    Select and return a random word from the list of words.
    The difficulty level determines the length of the word.
    """
    if difficulty == "easy":
        # Easy difficulty: choose shorter words (3-5 letters)
        filtered_words = [word for word in words if 3 <= len(word) <= 5]
    elif difficulty == "medium":
        # Medium difficulty: choose medium-length words (6-8 letters)
        filtered_words = [word for word in words if 6 <= len(word) <= 8]
    else:
        # Hard difficulty: choose longer words (9+ letters)
        filtered_words = [word for word in words if len(word) >= 9]

    return random.choice(filtered_words) if filtered_words else random.choice(words)


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
        return "correct", f"---- Good job! '{guess}' is in the word. ----"
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


def get_difficulty():
    """
    Ask the player to choose a difficulty level by entering a number: 1 (easy), 2 (medium), or 3 (hard).
    """
    while True:
        print("Choose a difficulty level by entering a number:")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        difficulty = input("Please enter 1, 2, or 3: ")

        if difficulty == "1":
            return "easy"
        elif difficulty == "2":
            return "medium"
        elif difficulty == "3":
            return "hard"
        else:
            print(
                "---- Invalid choice. Please enter 1 for easy, 2 for medium, or 3 for hard. ---- "
            )


def set_remaining_attempts(difficulty):
    """
    Set the number of remaining attempts based on the chosen difficulty level.
    """
    if difficulty == "easy":
        return 8  # More attempts for easier difficulty
    elif difficulty == "medium":
        return 6
    else:
        return 5  # Fewer attempts for harder difficulty


def hangman_game(word, remaining_attempts):
    """
    Main game loop for the Hangman game.
    Manages the game flow, receiving the word to guess as input.
    """
    guessed_letters = set()

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
