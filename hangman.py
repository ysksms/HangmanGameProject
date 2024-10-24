from functions import load_words, choose_random_word, hangman_game


def main():
    """
    Main function to load words, select a random word, and start the Hangman game.
    """
    words = load_words("words.txt")  # Load words from the file
    word = choose_random_word(words)  # Select a random word from the list
    hangman_game(word)  # Start the game with the chosen word


if __name__ == "__main__":
    main()
