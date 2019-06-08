import typr, time, replit, gamx as gg, metadata as inf

replit.clear();

print("|==============|")
print("|=!  Escape  !=|")
print("|=! OBLIVION !=|")
print("|==============|")

nm = 'Joe'

yess=["yes", "ye", "y", "yeet"]

def tutorial():
	replit.clear()
	typr.typr("Welcome to the tutorial!")
	time.sleep(0.5)
	typr.typr("When you are asked to make a choice in the game, please respond with '1', '2', or '3' (if applicable).")
	time.sleep(0.5)
	typr.typr("Let's try it out!")
	inf.parse("Option 1 (type 1)", "Option 2 (type 2)")
	typr.typr("Good job! Last one, and then you will be ready.")
	inf.parse3("Option 1 (type 1)", "Option 2 (type 2)", "Option 3 (type 3)")
	typr.typr("You are ready now! Let's begin.")
	time.sleep(1)
	replit.clear()

while(True):
	nm = input("State your name: ").strip()
	if(nm != ''):
		break

time.sleep(0.5)
xd = input("\nEnable typing effect? (Y/n) ").strip().lower()
if(xd in yess):
	typr.setVar(True)
else: typr.setVar(False)

time.sleep(0.5)
typr.typr("\nAlright, hello " + nm + "!")
tut = input("Do you want to play the tutorial? (Y/n) ").strip().lower()
if(tut in yess):
	tutorial()

def recheck():
	print("\nPlease select '1' or '2'.")
	lr = input(">> ");
	if(lr in inf.ones):
		gg.left(nm)
	elif(lr in inf.twos):
		gg.right(nm)
	else:
		recheck()

replit.clear()
time.sleep(1)


typr.typr("You wake up, confused, and find yourself in a dimly lit hallway... You don't remember anything at all, except that you need to escape from this place.")
time.sleep(0.5)
lr = input("--\n1 | Go left.\n2 | Go right.\n>> ").strip().lower()
if(lr in inf.ones):
	gg.left(nm)
elif(lr in inf.twos):
	gg.right(nm)
else:
	recheck()



