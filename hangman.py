import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")


# Fill with blank spaces
display = []
for letter in chosen_word:
    display.append("_")

# keeping track of the lives
lives_left = 6

while "_" in display:
    # keep track of new spaces filled
    blank_spaces_filled = 0

    # check if we have lives left
    if lives_left > 0:
        # Promt the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # replace blank spaces with guessed letter
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                blank_spaces_filled += 1

        # Check if we have new spaces filled. Otherwise we lose a life
        if blank_spaces_filled > 0:
            print(display)
        else:
            lives_left -= 1
            print(stages[lives_left])
    # Get out of the loop if we run out of lives
    else:
        break
# If we got out of the loop with lives left it means we've won. Otherwise it means we lost.
if lives_left > 0:
    print("You've won!")
else:
    print("Game over. You lose")
