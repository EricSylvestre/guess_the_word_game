import random

# Word List
words = ["coding", "computer", "technology", "keyboard", "python", "database", "software"]


print(f"Welcome to Guess the Word Game! ")
print(f"Guess one letter at a time to fill in the mystery word. ")
print(f"HINT: ALL MYSTERY WORDS ARE CODING & TECHNOLOGY WORDS. ")


running = True
while running:
    user_input = input(f"Are you ready to play?! Y/N ")
    if user_input == "Y":
        print("LETS PLAY! ")
        running = False
        
    elif user_input == "N":
        print("No Problem. ")
    
    
        
        


# choose random word from word list to be guessing word
random_word = random.choice(words)
# convert guessing word to underscores and spaces
display_word = ""
for i in random_word:
    display_word = display_word + "_ "

#--- check reamaining turns. 
turns = 7
previous_guesses = []
while turns > 0:
    
    # display underscores and spaces
    print(display_word)
    # take guess as letter
    guess = input(f"Guess a letter! ")

    # check if weve guessed this already
    if guess not in previous_guesses:
        previous_guesses.append(guess)
    else:
        print("You already guessed that! ")
        continue

    # check to see if the letter is in the guessing word
    if guess in random_word:
        
        #replace underscore(s) with that letter
        for random_word_index, letter in enumerate(random_word):
            if guess == letter:
                display_word_index = random_word_index * 2
                display_word_list = list(display_word)
                display_word_list[display_word_index] = guess
                display_word = "".join(display_word_list)

   
    
    # if letter is not in the word, take away a turn.
    else:
        print(f"You guessed incorrect! You lose a turn")
        turns -= 1
        print(f"You have {turns} remaining ")
   

    if "_" not in display_word:
        print("You beat me! Great job. ")
        break
    
if turns == 0:
    print(f"You lost HAHA! ")

