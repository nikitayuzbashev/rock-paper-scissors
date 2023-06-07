import rpsASCII  # Importing the module that contains ASCII art for rock, paper, and scissors
import random  # Importing the random module for generating random numbers

# List of ASCII art for each choice
choices = [rpsASCII.rock_art, rpsASCII.paper_art, rpsASCII.scissors_art]

print("Let's play Rock Paper Scissors!")

# Counter for player wins
player_wins = 0
# Counter for computer wins
computer_wins = 0

# Main game loop, continues until player chooses not to play anymore
while True:

    # Generate a random number to represent computer's choice
    computernumber = random.randrange(len(choices))

    # Loop to validate player's input
    while True:
        yournumber = int(input("Choose what you will play: 0 for rock, 1 for paper, 2 for scissors.\n"))
        # Check if player's input is within the valid range
        if yournumber in range(len(choices)):
            break
        else:
            print("Invalid entry.")

    # Get the ASCII art corresponding to player's choice
    yourchoice = choices[yournumber]
    # Get the ASCII art corresponding to computer's choice
    computerchoice = choices[computernumber]

    print(f"You chose:\n{yourchoice}\nComputer chose:\n{computerchoice}")

    # Check if it's a draw
    if yournumber == computernumber:
        print("Draw :/")
    # Check the winning conditions for the player
    elif (yournumber == 0 and computernumber == 2) or (yournumber == 1 and computernumber == 0) or (yournumber == 2 and computernumber == 1):
        print("You win :)")
        # Increment player's win counter
        player_wins += 1
    else:
        print("You lose :(")
        # Increment computer's win counter
        computer_wins += 1

    print(f"The score is {player_wins} : {computer_wins}.")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")
    # If the player chooses not to play again, exit the loop
    if play_again.lower() == "no":
        break

print("Thank you for playing!")
