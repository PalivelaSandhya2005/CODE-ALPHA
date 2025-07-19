import random
words = ["apple", "magic", "robot", "piano", "zebra"]
selected_word = random.choice(words)
guessed_letters = []
tries_left = 6
display_word = ["_"] * len(selected_word)
print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 wrong attempts. Good luck!\n")
while tries_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single alphabet letter.\n")
        continue
    if guess in guessed_letters:
        print("⚠ You already guessed that letter. Try another one.\n")
        continue
    guessed_letters.append(guess)
    if guess in selected_word:
        print("✅ Good guess!\n")
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                display_word[i] = guess
    else:
        tries_left -= 1
        print(f"❌ Wrong guess! Tries left: {tries_left}\n")
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", selected_word)
else:
    print("💀 Game Over! The word was:", selected_word)