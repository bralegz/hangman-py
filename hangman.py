import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")


# Fill with blank spaces
display = []
for letter in chosen_word:
    display.append("_")
    
while "_" in display:
    # Prompt user to
    guess = input("Guess a letter: ").lower()

    # replace blank spaces with letter
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess

    print(display)
    
print("You won!")
