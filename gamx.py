''' All of the game's code apart from the intro. '''

import replit
import random
import typr
import metadata as inf
import time

name = "Johnny"
hasKey = False
doors = ['1', '2']
good_door = random.choice(doors)

def win_end():
	typr.typr("You open the door and enter it. You almost faint. Your first breath of fresh air for a month.")
	time.sleep(1)
	print("|======================|")
	print("|=!     You have     !=|")
	print("|=! escaped OBLIVION !=|")
	print("|======================|\n")
	typr.typr("Congratulations! You have successfully escaped Oblivion!")

def win():
	typr.typr("A water landing? Lucky you can swim well.")
	time.sleep(0.5)
	typr.typr("Your pocket begins to glow. You look inside and realize... it's the key! It looks like it's pointing in a certain direction.")
	time.sleep(0.5)
	replit.clear()
	typr.typr("Suddenly, the key stops glowing. There are two doors up ahead. The right choice would get you home safe, the other would do the opposite.")
	time.sleep(0.5)
	typr.typr("Choose wisely...")
	choice = inf.parse("The left door.", "The right door.")
	if(choice == good_door):
		replit.clear()
		win_end()
	else:
		inf.endGameTwoLn("Sometimes, life is a game of chance", "The odds were not in your favor, my friend. Oblivion has won.")

def floatPit():
	typr.typr("That was a remarkably smooth landing, but you can't fly anymore.")
	if(hasKey == False):
		time.sleep(0.5)
		typr.typr("WHAT!!! Water?? But... but... You can't swim!!!!")
		inf.endGameTwoLn("You drown in the water.", "The End?")
	else: win()


def pit():
	typr.typr("That was some fall, but you were saved.")
	if(hasKey == False):
		time.sleep(0.5)
		typr.typr("A water landing??? But... but... You can't swim!!!!")
		inf.endGameTwoLn("You drown in the water.", "The End?")
	else:
		win()
		
def jumpPit():
	typr.typr("You prepare for the worst and decide to jump.")
	time.sleep(0.5)
	typr.typr("3...2...1...JUMP!", 0.25)
	time.sleep(1)
	pit()


def turnBack():
	typr.typr("You turn around to find that your exit is blocked! You have to jump.")
	time.sleep(0.5)
	jumpPit()
	

def climbStairs():
	typr.typr("You sprint up the staircase, lose your balance, and almost fall over when you reach the end. A bottomless pit... Well, almost. You see a small light shining at the very bottom of the pit... Your way out? Possibly...")
	choice = inf.parse("Jump in!", "Turn back.")
	if(choice in inf.ones): jumpPit()
	else: turnBack()

def jumpDownLadderChoice():
	typr.typr("If you jump, you wouldn't be able to make it.")
	choice = inf.parse("Jump (I don't know why you would do this).", "Climb the staircase. (The logical choice).")
	if(choice in inf.ones):
		inf.endGameTwoLn("I was right, wasn't I?", "You are left immobilzed due to the impact damage. Oblivion has won. The end?")
	else: climbStairs()


def climbFaster():
	typr.typr('You reach the top of the ladder, barely. You see a lit up staircase to your left...')
	time.sleep(0.5)
	choice = inf.parse("Climb the staircase.", "Jump back down.")
	if(choice in inf.ones): climbStairs()
	else: jumpDownLadderChoice()


def climbLadderB():
	typr.typr("You start to climb the ladder, but when you get about halfway up, the rungs start to fall off. Don't jump off, or the walls will get you...")
	time.sleep(0.5)
	choice = inf.parse("Trust your instincts and climb faster.", "Jump off and accept defeat.")
	if(choice in inf.ones):
		climbFaster()
	else:
		inf.endGame("The walls cave in on you until silence is all that remains. Oblivion has won. The end?")

def investigateNoise():
	typr.typr("You look around, and find an almost completely camouflaged ladder. You start to climb it, but when you get about halfway up the ladder, the rungs begin to fall down...")
	time.sleep(0.5)
	choice = inf.parse("Jump off while you still can.", "Trust your instincts and climb faster.")
	if(choice in inf.ones):
		inf.endGameTwoLn("You jump off the ladder, landing on... the floor? You hit nothing but keep falling, as if the floor had slid down.", "When you finally hit the ground, impact damage leaves you immobilized. Oblivion has won. The end?")
		return
	else:
		climbFaster()

def getKey():
	# Get the key.
	return

def pressRedButton():
	typr.typr("The floor disappears below you, and you start to fall. At least the walls won't hurt you...")
	time.sleep(1)
	typr.typr("You think it's been about 2 hours since you started falling, when, to your surprise, you start floating upwards. It's as if... you can fly!")
	time.sleep(0.5)
	choice = inf.parse("Attempt to fly back up", "Float to the bottom of the hole.")
	if(choice in inf.ones):
		typr.typr("The walls closed in on you, remember? You float to the bottom of the hole.")
		floatPit()
	else:
		floatPit()

def continueLeft():
		typr.typr("You trip over something. A trap? The walls begin to cave in...")
		time.sleep(0.5)
		choice = inf.parse("Go back and climb the odd ladder you saw.", "Hit the suspicious red button you see next to you.")
		if(choice in inf.ones):
			climbLadderB()
		else:
			pressRedButton()

def exitDoor1():
		typr.typr("You fall over. A booby-trap? The ceiling begins to slide down...")
		time.sleep(0.5)
		choice = inf.parse3("Go into the second door.", "Look around.", "Run left.")
		if(choice in inf.ones):
			enterDoor2()
		elif(choice in inf.twos): investigateNoise()
		else:
			continueLeft()


def enterDoor1Choice():
	global hasKey
	if(hasKey == False):
		typr.typr("You found a key!")
		time.sleep(0.5)
		typr.typr("You pick it up. You look around, nothing else here.")
		hasKey = True
	else:
		typr.typr("We've been here already.")
	choice = inf.parse("Turn back.", "Jump for joy immaturely.")
	if(choice in inf.ones):
		exitDoor1()
	else:
		inf.endGameTwoLn("You (for some reason) decide to jump for joy, but realize too late that the floor is very unstable.", "Oblivion has won (by accident this time). The end?")

def enterDoor2():
	if(hasKey == True):
		typr.typr("You run into Door 2 and find a staircase leading down. You follow it for about 15 minutes until you find a locked door. You remember your key!")
		time.sleep(0.5)
		typr.typr("You use the key and it fits!")
		time.sleep(1)
		replit.clear()
		print("|======================|")
		print("|=!     You have     !=|")
		print("|=! escaped OBLIVION !=|")
		print("|======================|\n")
		typr.typr("Congratulations! You have successfully escaped Oblivion!")
	else:
		typr.typr("Oops! I think you may have taken a wrong turn. Ahhhh! Watch Ouuu...")
		print("--")
		inf.endGameTwoLn("Caught you by surprise, have I?", "\t--- Oblivion")


def flipSwitches():
		typr.typr("You flip two switches, and a door opens up behind you. You flip the other two, and another one opens in front of you! Either one could get you out, or to Oblivion...")
		time.sleep(0.5)
		choice = inf.parse("Enter Door 1", "Enter Door 2")
		if(choice in inf.ones):
			enterDoor1Choice()
		else:
			enterDoor2()

def runBackLeft():
	typr.typr("You sprint in the other direction but trip over something. A trap? The walls begin to cave in...")
	time.sleep(0.5)
	choice = inf.parse("Go back and climb the odd ladder you saw.", "Hit the suspicious red button you see next to you.")
	if(choice in inf.ones):
		climbLadderB()
	else:
		pressRedButton()


def lightAllCandles():
	typr.typr("You light two candles, and suddenly... Two doors open up.")
	time.sleep(0.5)
	choice = inf.parse("Enter Door 1", "Enter Door 2")
	if(choice in inf.ones):
		enterDoor1Choice()
	else:
		enterDoor2()


def investigateNoiseB():
	investigateNoise()

def blowOutCandles():
	typr.typr("Well that didn't help anyone. Now you're in the dark, and alone... well, except for that screeching noise...")
	time.sleep(0.5)
	choice = inf.parse("Investigate", "Run the other way.")
	if(choice in inf.ones):
		investigateNoiseB()
	else:
		runBackLeft()

def goToCandles():
	typr.typr("You walk towards the candles and find 23 of them, and a few matches. Only 18 candles are lit up...")
	time.sleep(0.5)
	choice = inf.parse("Light the rest of the candles.", "Blow out all of the candles")
	if(choice in inf.ones):
		lightAllCandles()
	else:
		blowOutCandles()

def right2():
	typr.typr("You go right to find a dead end and an array of switches, but there are no lightbulbs, only candles lit up in the corner.")
	time.sleep(0.5)
	choice = inf.parse("Flip the switches.", "Go find the candles.")
	if(choice in inf.ones):
		flipSwitches()
	else:
		goToCandles()

def left2():
	typr.typr("You walk left and stop abruptly after hearing a creaking noise from above...")
	time.sleep(0.5)
	choice = inf.parse3("Investigate.", "Continue going left.", "Go right instead.")
	if(choice in inf.ones):
		investigateNoise()
	elif(choice in inf.twos):
		continueLeft()
	else: right2()

def left(nm):
	global name
	name = nm
	replit.clear()
	left2()

def right(nm):
	global name
	name = nm
	replit.clear()
	right2()


