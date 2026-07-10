import random

# Predefined list of words
words = ["apple", "tiger", "chair", "robot", "green"]

# Randomly choose a word
word = random.choice(words)

# Create a list to display guessed letters
guessed_word = ["_"] * len(word)

# Track guessed letters
guessed_letters = []

# Limit incorrect guesses
attempts = 6

print("🎯 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(" ".join(guessed_word))

# Game loop
while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)