# Importing the 'logo' from the 'art' module
from art import logo

# Displaying the logo
print(logo)

# List of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Flag to control the game loop
end_game = False

# Game loop
while end_game == False:
    # Taking input from the user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26                      # Ensuring the shift value is within the range of the alphabet

    # Setting up a flag if the user enters the correct shift number
    more = False

    # Function to perform Caesar cipher
    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        l_alphabet = len(alphabet) - 1

        for char in start_text:
            # Check if the character is an alphabet
            if char.isalpha():
                position = alphabet.index(char)
                if cipher_direction == "decode":
                    new_position = position - shift_amount
                    new_letter = alphabet[new_position]
                    end_text += new_letter
                else:
                    new_position = shift_amount + position
                    if new_position > l_alphabet:
                        rev_position = (new_position - l_alphabet - 1)
                        new_letter = alphabet[rev_position]
                        end_text += new_letter
                    else:
                        new_letter = alphabet[new_position]
                        end_text += new_letter
            else:
                end_text += char
        print(f"THE {cipher_direction}d text is {end_text}")

    # Calling the Caesar cipher function
    caesar(text, shift, direction)

    # Asking the user if they want to continue the game
    play_again = input("Do you want to continue the game? (Y/N)\n").lower()

    # Updating the flag based on user input
    if play_again == "y":
        end_game = False
    else:
        print("Thank you for participating! Hope you enjoyed it!")
        end_game = True