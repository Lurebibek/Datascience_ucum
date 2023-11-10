# Importing necessary modules
import os
from art import gavel

# Setting up initial variables
end_game = True
bid_sheet = {}  # Dictionary to store bids
temp_sheet = {}  # Temporary dictionary to store bids during the game

# Function to update bid_sheet with a new bid
def bid_war(name, bid):
    temp_sheet[name] = bid  # Store the bid in the temporary sheet during the game
    bid_sheet[name] = bid  # Store the bid in the final bid sheet
    return bid_sheet

# Function to determine the winner based on the highest bid
def winner(bid_sheet):
    highest_bid = 0
    highest_bidders = {}  # Dictionary to store the highest bidder(s)
    
    # Iterate through bid_sheet to find the highest bid and bidder(s)
    for key, value in bid_sheet.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidders = {key: value}
    
    # Print the winner(s)
    for key, value in highest_bidders.items():
        print(f"The winner from the auction is {key} with a bid of ${value}.")

# Game loop
while end_game == True:
    os.system('clear')  # Clear the console screen
    print(gavel)  # Display the gavel art
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_war(name, bid)  # Record the bid
    
    m_play = input("Do you have more bidders? (Y/N) ").lower()
    if m_play == "y":
        end_game = True
    else:
        end_game = False

# Call the winner function to determine and print the winner(s)
winner(bid_sheet)

# Print the temporary bid sheet
print(temp_sheet)
