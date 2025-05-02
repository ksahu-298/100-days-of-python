# Hangman Game in Python 
import random

# List of words to choose from
words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

# Function to start the game
def start_game():
    word = random.choice(words)
    word_length = len(word)
    guesses = ''
    attempts = word_length + 2  # Number of attempts the player gets

    print("The word has", word_length, "letters.")
    
    while attempts > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        
        if failed == 0:
            print("\nYou won!")
            break
        
        guess = input("\nGuess a letter: ")
        guesses += guess
        
        if guess not in word:
            attempts -= 1
            print("Wrong guess. You have", attempts, "attempts left.")
        
        if attempts == 0:
            print("\nYou lost. The word was", word)

if __name__ == "__main__":
    start_game()
