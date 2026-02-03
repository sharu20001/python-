import random

def choose_word():
    # List of words to guess
    words = ["python", "programming", "hangman", "developer", "computer", "algorithm"]
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of allowed wrong attempts

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Display current state of the word
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

        # Check if the player has won
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
