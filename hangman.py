from functions import (
    load_words,
    choose_random_word,
    hangman_game,
    get_difficulty,
    set_remaining_attempts,
)


def main():
    """
    Main function to load words, select a random word based on difficulty, and start the Hangman game.
    """

    # Load words from the file
    words = load_words("words.txt")

    # Ask the player to choose the difficulty level
    difficulty = get_difficulty()

    # Select a random word based on the chosen difficulty
    word = choose_random_word(words, difficulty)

    # Set the number of remaining attempts based on difficulty
    remaining_attempts = set_remaining_attempts(difficulty)

    # Start the game with the chosen word and remaining attempts
    hangman_game(word, remaining_attempts)


if __name__ == "__main__":
    main()
