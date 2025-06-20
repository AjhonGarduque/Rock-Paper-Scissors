import random # Import the random module to let the computer choose randomly

print("Welcome to Rock, Paper, Scissors!")

player_score = 0   # player's score
computer_score = 0 # computer's score

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
            computer_score += 1 # adds 1 point to the computer
        else:  # computer_choice == "scissors"
            print("Result: You win!")
            player_score += 1   # adds 1 point to the player

    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Result: You lose!")
            computer_score += 1 # adds 1 point to the computer
        else:  # computer_choice == "rock"
            print("Result: You win!")
            player_score += 1   # adds 1 point to the player

    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Result: You lose!")
            computer_score += 1 # adds 1 point to the computer
        else:  # computer_choice == "paper"
            print("Result: You win!")
            player_score += 1  # adds 1 point to the player

    print("") 
    print(f"SCORE: Player: {player_score} | Computer: {computer_score}") # Displays the score of the player and computer after each round

    #Ask player if they want to play again
    play_again = input("\nWould you like to play again? (Y/N): ").strip().lower()
    #Exit the game loop if player enters anything other than 'y'
    if play_again != 'y':
        break

# Displays the final score after the game
print("\nFinal Score:")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")

# Prints a message depending on the final score
if player_score > computer_score:
    print("\nYou Win!")
elif player_score < computer_score:
    print("\nYou Lose")
else:
    print("It's a tie")

print("\nThank you for playing! Goodbye.")
