import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")


# Fill with blank spaces
display = []
for letter in chosen_word:
    display.append("_")

lives_left = 6

while "_" in display:
    blank_spaces_filled = 0
    if lives_left > 0:
        # Prompt user to
        guess = input("Guess a letter: ").lower()

        # replace blank spaces with letter
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                blank_spaces_filled += 1
        if blank_spaces_filled > 0:
            print(display)
        else:
            print("Wrong!")
            lives_left -= 1
    else:
      break

if lives_left > 0:      
    print("You've won!")
else:
    print("Game over. You lose")
