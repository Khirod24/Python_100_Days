#HANGMAN GAME 
import random
from Hangman_words import word_list
from Hangman_art import stages,logo

choosen_word = random.choice(word_list)
word_length = len(choosen_word)

end_of_game = False
lives = 6

print(logo)

#testing code
# print(f"The chosen word is: {choosen_word}")

display=[]
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!!")

    if "_" not in display:
        end_of_game = True
        print("You Win!!")
    
    print(stages[lives])