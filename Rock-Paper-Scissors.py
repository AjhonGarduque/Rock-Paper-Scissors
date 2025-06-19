import random # Import the random module to let the computer choose randomly

print("Welcome to Rock, Paper, Scissors!")

# Main game loop (keeps repeating until player decides to quit)
while True:
    choices = ['rock', 'paper', 'scissors']         #Possible choices
    computer_choice = random.choice(choices)        #Randomly selects the computer's move
    player_choice = None                            #Initialize player's choice

    #Keeps asking until the player enters a valid choice
    while player_choice not in choices:
        player_choice = input("Please enter your choice (rock, paper, or scissors): ").lower()

    #Display both player's and computer's choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    #Compare choices to determine the result
    if player_choice == computer_choice:
        print("Result: It's a tie!")

    elif player_choice == "rock":
        if computer_choice == "paper":
            print("Result: You lose!")
        else:  # computer_choice == "scissors"
            print("Result: You win!")

    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Result: You lose!")
        else:  # computer_choice == "rock"
            print("Result: You win!")

    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Result: You lose!")
        else:  # computer_choice == "paper"
            print("Result: You win!")

    #Ask player if they want to play again
    play_again = input("\nWould you like to play again? (Y/N): ").strip().lower()
    #Exit the game loop if player enters anything other than 'y'
    if play_again != 'y':
        break

print("\nThank you for playing! Goodbye.")
