import random

words = ["apple", "tiger", "house", "chair", "robot"]

word = random.choice(words)

guessed = []
wrong = 0

display = ["_"] * len(word)

print("HANGMAN GAME")

while wrong < 6 and "_" in display:

    print("\nWord:", " ".join(display))

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        wrong += 1

if "_" not in display:
    print("\nYou Win!")
else:
    print("\nGame Over")
import random

words = ["apple", "tiger", "house", "chair", "robot"]

word = random.choice(words)

guessed = []
wrong = 0

display = ["_"] * len(word)

print("HANGMAN GAME")

while wrong < 6 and "_" in display:

    print("\nWord:", " ".join(display))

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        wrong += 1

if "_" not in display:
    print("\nYou Win!")
else:
    print("\nGame Over")

print("Word was:", word)
print("Word was:", word)
