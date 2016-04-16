# import the necessary random number generator module
from random import randint

# print the game's "opening"
print("Welcome to Cycle!")
print("You have stolen a bicycle in the mad max apocalypse.")
print("The punks want their bicycle back and are chasing you down.")
print("Can you survive the apocalypse and outrun the punks?")

# the game is not done
done = False

# these are the game's main variables
miles_traveled = 0
thirst = 0
fatigue = 0
punks_distance = -20
drinks = 3

# this is the main loop of the game.
while not done:
	print("A: Drink from your canteen.")
	print("B: Ahead moderate speed.")
	print("C: Ahead full speed.")
	print("D: Stop for the night.")
	print("E: Status check.")
	print("Q: Quit.")
	if thirst > 4:
		print "You are thirsty."
	elif thirst > 6:
		print "You have died of thirst."
		done = True
	
	if not done and fatigue > 5:
		print "You are getting tired."
	elif not done and fatigue > 8:
		print "You have died of fatigue."
		done = True
		
	if not done and punks_distance > (miles_traveled - 15):
		print "The punks are getting close!"
	elif not done and punks_distance > miles_traveled:
		print "The punks have captured you!"
		done = True
	
	if not done and miles_traveled > 200:
		print "You have escaped into the desert! You win!"
		done = True
	
	oasis = randint(1, 20)
	if not done and oasis >20:
		print "You have found a beautiful oasis! You rest for a moment."
		thirst = 0
		fatigue = 0
		drinks = 3
	
	choice = raw_input("> ")
	if choice.upper() == "Q":
		done = True
	elif choice.upper() == "E":
		punks_behind = abs(miles_traveled - punks_distance)
		print "Miles traveled:", miles_traveled
		print "Drinks in canteen:", drinks
		print "The punks are", punks_behind, "miles behind you."
	elif choice.upper() == "D":
		print("Your sore calves feel rested.")
		print("But you are worried that the punks are approaching.")
		fatigue = 0
		punks_distance = punks_distance + randint(7, 14)
	elif choice.upper() == "C":
		speed = randint(10, 20)
		miles_traveled = miles_traveled + speed
		print "You traveled", speed, "miles!"
		thirst = thirst + 1
		fatigue = fatigue + randint(1, 3)
		punks_distance = punks_distance + randint(7, 14)
	elif choice.upper() == "B":
		speed = randint(5, 12)
		miles_traveled = miles_traveled + speed
		print "You traveled", speed, "miles!"
		thirst = thirst + 1
		fatigue = fatigue + 1
		punks_distance = punks_distance + randint(7, 14)
	elif choice.upper() == "A":
		if drinks > 0:
			print "You take a long drink from your canteen."
			thirst = 0
			drinks = drinks -1
		elif drinks == 0:
			print "You have no more water."