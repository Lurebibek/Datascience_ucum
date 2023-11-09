

import random
from reprlib import clear
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

# randomly choosinf the word from the list


import random


# Choose the random word from the list
chosen_word=random.choice(word_list)
print(chosen_word)


r_word=[]

for letter in chosen_word:
    r_word.append(letter)





#Testing code
print(f'Pssst, the solution is {chosen_word}.')


#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


display=[]
for letter in chosen_word:
    display.append("_")
print(display)


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
end_game=False
chance=len(stages)
while end_game==False :
    guess= (input("Guess the letter. ").lower())
    clear()
    if guess not in r_word:
        chance-=1 
        print(stages[chance])
        print(f"You have {chance} chance left ")
        if chance==0:
            print("You Loose")
            end_game=True
    else:
        for x in range (len(chosen_word)):
            if chosen_word[x]==guess:
                display[x]=guess
                r_word.remove(guess)
            
    print(display)
    
    if "_" not in display and chance>0:
        print("you Win")
        end_game=True
    
    











