"""
this is a small program that serves the purpose to
refresh some of my python skills
"""
from random import choice
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
computer_list = [ROCK, PAPER, SCISSORS]
def wincheck(player, computer):
    """
    In this function it is checked if the player
    won or didn't  won by returning True, false
    or draw as a string
    """
    if player == computer:
        return "draw"
    #the following if statements check if the player lost
    if (player == ROCK and computer == PAPER):
        return False
    if (player == PAPER and computer == SCISSORS):
        return False
    if (player == SCISSORS and computer == ROCK):
        return False
    return True
        #who came up with 50 chars per comment
def human_readable_converter(computer):
    """
    In here the r, p and s are converted
    into more understandable words
    """
    if computer == ROCK:
        return "Rock"
    if computer == PAPER:
        return "Paper"
    if computer == SCISSORS:
        return "Scissors"
    raise Exception(f"Not translatable input detected \"{computer}\" "
    "please check what has gone wrong")
def main():
    """
    Main part of the Program
    """
    again = True
    print("The rules of this game are easy"
    " \nRock beats Scissors"
    " \nPaper beats Rock"
    " \nScissors beats Paper")
    while again:
        print("Please pick your choice: ")
        player_input = input()
        again = False
        wrong_message = player_input
        try:
            player_input = player_input[0].lower()#in here we will take the first char
                                                  #of the players input and lower it
            player_false_input = False #dont you love it when you type Flase instead of False
        except IndexError:
            print("You know you have input something instead of just pressing enter")
            player_false_input = True
        if player_false_input is False and True:
            computer_choice = choice(computer_list)
            result = wincheck(player_input ,computer_choice)
            print(f"You used {wrong_message}")
            print(f"Your Opponent used {human_readable_converter(computer_choice)}")
            if result == "draw":
                print("Neither of you won")
            elif result is False:
                print("You lost")
            elif result:
                print("You won")
            print("\n\nDo you want to try again (Y/N)")
            answer = input()[0].lower()
            if answer == "y":
                again = True
            elif answer == "n":
                again = False
            else:
                print("Your answer is no valid answer")
                print("Exiting....")
        else:
            print(f"Please input Rock, Paper or Scissors instead of \"{wrong_message}\"")
            #The player should know that he did #something wrong
            again = True

if __name__ == "__main__":
    main()
    