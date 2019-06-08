'''Self Created LIB FOr Smooth Typing Effect'''

import time, sys

eff = True

def typr(text, wait = 0.05, prefix = "", suffix = ""):
	if(eff):
		for char in text:
			print(prefix + char + suffix, sep=' ', end='', file=sys.stdout, flush=True) 
			time.sleep(wait)
		print("")
	else:
		print(prefix + text + suffix) 
	
def setVar(tf):
	global eff
	eff = tf
