#12345678901234567890123456789012345678901234567890
#this is a small program that serves the purpose to
#refresh some of my python skills
from random import choice
PlayerI = ""
PlayerF = False
Again = True
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
PCList = [ROCK, PAPER, SCISSORS]
def wincheck(PL, PC):
	"""
	In this function it is checked if the player
	won or didn't  won by returning True, false
	or draw as a string 
	(cause this isn't quantum computing where
	there is something beetwen true and false)
	"""
	if PL == PC:
		return "draw"
	elif (PL == ROCK and PC == PAPER) or (PL == PAPER and PC == SCISSORS) or (PL == SCISSORS and PC == ROCK): #In here it is checked if the player lost
		return False
	elif (PC == ROCK and PL == PAPER) or (PC == PAPER and PL == SCISSORS) or (PC == SCISSORS and PL == ROCK): #and in here we check if the player won
		return True
	else: #
		raise Exception(f"Something has gone wrong please check the if statments \nPlayerInput\"{PL}\" \n PCInput\"{PC}\"") 
		#I am scared that my if statements are wrong
		#so that it will instead run ahead it will
		#be easier to debug if i will raise an
		#exception in here

		#who came up with 50 chars per comment
def HumanReadable(PC):
	"""
	In here the r, p and s are converted
	into more understandable words
	"""
	if PC == ROCK:
		return "Rock"
	elif PC == PAPER:
		return "Paper"
	elif PC == SCISSORS:
		return "Scissors"
	else:
		raise Exception(f"Not translatable input detected \"{PC}\"  please check what has gone wrong")
print("The rules of this game are easy \nRock beats Scissors \nPaper beats Rock \nScissors beats Paper")
while Again == True:
	print("Please pick your choice: ")
	PlayerI = input()
	Again = False
	WrongMessage = PlayerI
	try:
		PlayerI = PlayerI[0].lower() #in here we will take the first char
					     #of the players input and lower it
		PlayerF = False #dont you love it when you type Flase instead of False
	except IndexError:
		print("You know you have input something instead of just pressing enter")
		PlayerF = True
	if PlayerF == False and ((PlayerI == ROCK) or (PlayerI == PAPER) or (PlayerI == SCISSORS)) == True:
		PCchoice = choice(PCList)
		Result = wincheck(PlayerI ,PCchoice)
		print(f"You used {WrongMessage}")
		print(f"Your Opponent used {HumanReadable(PCchoice)}")
		if Result == "draw":
			print("Neither of you won")
		elif Result == False:
			print("You lost")
		elif Result == True:
			print("You won")
		else:
			print("???")
			raise Exception("???") #I once had something like this happen
					       #I dont knwo how this happened but if
					       #it happens again then i will know
					       #that it happened
		print("\n\nDo you want to try again (Y/N)")
		Answer = input()[0].lower()
		if Answer == "y":
			Again = True
		elif Answer == "n":
			Again = False
		else:
			print("Your answer is no valid answer")
			print("Exiting....")
	else:
		print(f"Please input Rock, Paper or Scissors instead of \"{WrongMessage}\"") #The player should know that he did 
											     #something wrong
		Again == True
