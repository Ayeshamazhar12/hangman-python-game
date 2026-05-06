import random

# Hangman stages (UI)
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

# Word categories
easy_words = ["cat", "dog", "sun"]
medium_words = ["apple", "tiger", "chair"]
hard_words = ["python", "planet", "rocket"]


def choose_word():
    print("\n🎯 Select Difficulty:")
    print("1. Easy\n2. Medium\n3. Hard")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return random.choice(easy_words)
    elif choice == "3":
        return random.choice(hard_words)
    else:
        return random.choice(medium_words)


def play_game():
    word = choose_word()
    guessed_word = ["_"] * len(word)
    guessed_letters = []

    wrong_guesses = 0
    max_wrong = 6
    hint_used = False

    print("\n" + "=" * 35)
    print("🎮 HANGMAN GAME STARTED 🎮")
    print("=" * 35)

    while wrong_guesses < max_wrong and "_" in guessed_word:

        print(stages[wrong_guesses])
        print("\n🧩 Word:", " ".join(guessed_word))

        if guessed_letters:
            print("🔤 Used letters:", ", ".join(guessed_letters))
        else:
            print("🔤 No guesses yet.")

        print(f"❤️ Lives left: {max_wrong - wrong_guesses}")

        # Hint system
        if not hint_used:
            use_hint = input("💡 Want a hint? (y/n): ").lower()
            if use_hint == "y":
                print(f"👉 Hint: The word starts with '{word[0]}'")
                hint_used = True

        guess = input("\n👉 Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("✅ Correct!")

            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

    # Final result
    print(stages[wrong_guesses])

    if "_" not in guessed_word:
        print(f"\n🎉 YOU WIN! The word was: {word}")
    else:
        print(f"\n💀 YOU LOST! The word was: {word}")


# Game loop (Replay feature)
while True:
    play_game()

    again = input("\n🔁 Play again? (y/n): ").lower()
    if again != "y":
        print("\n👋 Thanks for playing!")
        break