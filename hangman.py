import random


# Function to load words from a file
def load_words(file_path):
    """
    Load a list of words from the given file and return them as a list.
    Each word should be on a new line in the file.
    """
    with open(file_path, "r") as file:
        words = file.readlines()
    return [word.strip() for word in words]


# Function to select a random word from the list of words
def choose_random_word(words):
    """
    Select and return a random word from the list of words.
    """
    return random.choice(words)


# Function to display the current state of the guessed word
def display_word_state(word, guessed_letters):
    """
    Display the word with underscores for unguessed letters and reveal
    correctly guessed letters.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Function to run the main game loop
def hangman_game(word):
    """
    Main game loop for the Hangman game.
    Handles user input, tracks guessed letters, and checks win/lose conditions.
    """
    guessed_letters = set()
    remaining_attempts = 6
    word_length = len(word)

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    while remaining_attempts > 0:
        # Display the current word state
        current_state = display_word_state(word, guessed_letters)
        print(f"\nCurrent word: {current_state}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses remaining: {remaining_attempts}")

        # Ask the player for a letter
        guess = input("Guess a letter: ").lower()

        # Input validation: check if the letter was already guessed or is invalid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            remaining_attempts -= 1  # Decrease attempts for incorrect guess

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")


# Main function to start the game
def main():
    """
    Main function to load words, select a random word, and start the Hangman game.
    """
    words = load_words("words.txt")
    word = choose_random_word(words)
    hangman_game(word)


# Run the game
if __name__ == "__main__":
    main()
