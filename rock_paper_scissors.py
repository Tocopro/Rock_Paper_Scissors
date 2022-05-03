from random import randint

# a list of play options
p = ["Rock", "Paper", "Scissors"]

computer = p[randint(0, 2)]

# set player to false
player = False
while player == False:

    # set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Loose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You loose! ", computer, " cut ", player)
        else:
            print("You win! ", player, " covers ", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Loose ....", computer, " smashes ", player)
        else:
            print("You win! ", player, " cut ", computer)
    else:
        print("That is not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = p[randint(0, 2)]
