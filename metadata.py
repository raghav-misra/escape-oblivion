''' Basic data and reusable functions.'''

import time
import typr

ones = ["1", "a", "one"]
twos = ["2", "b", "two"]
threes = ["3", "c", "three"]

def parse3(option1, option2, option3):
	print("--")
	lr = input(f"1 | {option1}\n2 | {option2}\n3 | {option3}\n>> ").strip().lower()
	if(lr in ones):
		print("--")
		return "1"
	elif(lr in twos):
		print("--")
		return "2"
	elif(lr in threes):
		print("--")
		return "3"
	else:
		while(True):
			print("\nPlease select '1' or '2' or '3'.")
			lr = input(">> ").strip().lower()
			if(lr in ones):
				print("--")
				return "1"
			elif(lr in twos):
				print("--")
				return "2"
			elif(lr in threes):
				print("--")
				return "3"
			else:
				continue

def parse(option1, option2):
	print("--")
	lr = input(f"1 | {option1}\n2 | {option2}\n>> ").strip().lower()
	if(lr in ones):
		print("--")
		return "1"
	elif(lr in twos):
		print("--")
		return "2"
	else:
		while(True):
			print("\nPlease select '1' or '2'.")
			lr = input(">> ").strip().lower()
			if(lr in ones):
				print("--")
				return "1"
			elif(lr in twos):
				print("--")
				return "2"
			else:
				continue

def endGame(death):
	typr.typr(death + "\n--")

def endGameTwoLn(death1, death2):
	typr.typr(death1)
	time.sleep(0.5)
	typr.typr(death2)
	print("--")
