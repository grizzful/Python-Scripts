import random

# Function used to get user's choice
def get_user_choice():
    choice = input("Enter your choice (Rock/Paper/Scissors): ")
    while choice.lower() not in ['rock', 'paper', 'scissors']:
        choice = input("Invaild option. Please enter again (Rock/Paper/Scissors): ")
    return choice

def get_bot_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function used to decide the winner
def decide_winner():
    if user_choice == bot_choice:
        print("It is a tie!")
    elif user_choice == "rock":
        if bot_choice == "scissors":
            win = "User"
        else:
            win = "bot"

    elif user_choice == "paper":
        if bot_choice == "rock":
            win = "User"
        else:
            win = "bot"

    elif user_choice == "scissors":
        if bot_choice == "paper":
            win = "User"
        else:
            win = "bot"
    return win

# Start of main program
user_choice = get_user_choice()
bot_choice = get_bot_choice()
winner = decide_winner()
print("You picked:", user_choice)
print("The bot picked:", bot_choice)
print("The winner is:", winner)
