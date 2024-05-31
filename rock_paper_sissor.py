import random 

player_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        quit()
    if user_input == ["rock", "paper", "scissors"]:
        continue
    else:
        print("Sorry looks like your input is not valid :(")

    random_number = random.randint(0, 2)
    computer_chose = options[random_number]
    print("Computer picked", computer_chose + ".")

    if user_input == "rock" and computer_chose == "scissors":
        print("Yay!! you win!!")
        player_wins += 1

    elif user_input == "scissors" and computer_chose == "paper":
        print("Yay!! you win!!")
        player_wins += 1

    elif user_input == "paper" and computer_chose == "rock":
        print("Yay!! you win!!")
        player_wins += 1

    elif user_input == computer_chose:
        print("Looks like its a tie")

    else:
        print("Awwww, Looks like you lost:(")
        computer_wins += 1
    


print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbyee!")