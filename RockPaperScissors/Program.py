#12345678901234567890123456789012345678901234567890
#this is a small program that serves the purpose to
#refresh some of my python skills
from random import choice
scorePL = 0
scorePC = 0
PCList = ["r", "p", "s"]
PlayerI = ""

ROCK = "r"

PAPER = "p"

SCISSORS = "s"

print("The rules of this game are easy /nRock beats Scissors /nPaper beats Rock /nScissors beats Paper")

label start

print("So pick your choice: ")

PlayerI = input()

PlayerI = PlayerI[0].lower()

if (PlayerI != ROCK) or (PlayerI != PAPER) or (PlayerI != SCISSORS):
	#TODO: Add loop and finish this

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
	elif (PL == ROCK and PC == PAPER) or (PL == PAPER and PC == SCISSORS) or (PL == SCISSORS and PC == "ROCK"):
		return False
	elif (PL == ROCK and PC == SCISSORS) or (PL == PAPER and PC == ROCK) or (PL == SCISSORS and PC == PAPER):
		return true
	else:
		raise Exception("Something has gone wrong please check the if statments") 
		#I am scared that my if statements are wrong
		#so that it will instead run ahead it will
		#be easier to debug if i will raise an
		#exception in here

		#who came up with 50 chars per comment

