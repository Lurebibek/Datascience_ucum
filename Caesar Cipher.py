

 # imorting the the art called logo from art file
from art import logo    

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_game=False

while end_game==False :

 # Taking  the input from the user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26

    # setting up the if the user enter the correct shift number
    more=False
    def caesar(start_text,shift_amount,cipher_direction):
            end_text=""
            l_alphabet=((len(alphabet))-1)

            for char in start_text:
                if char.isalpha():
                    position=alphabet.index(char) 
                    if cipher_direction=="decode":
                        new_position=position-shift_amount
                        new_letter=alphabet[new_position]
                        end_text+=new_letter
                        
                    else:
                        new_position=shift_amount+position
                        if new_position>l_alphabet:
                            rev_position= (new_position-l_alphabet-1)
                            new_letter=alphabet[rev_position] 
                            end_text+=new_letter
                
                        else:
                            new_letter=alphabet[new_position]
                            end_text+=new_letter
                else:
                    end_text+=char
            print(f"THE {cipher_direction}d text is {end_text}")
    caesar(text,shift,direction)
    play_again=(input("you want to continue game (Y/N) ?\n")).lower()

    if play_again=="y":
        end_game=False
    else:
        print("Thank you for the participation hope you enjoyed it!")
        end_game=True
        


   





    
                    
    





    

