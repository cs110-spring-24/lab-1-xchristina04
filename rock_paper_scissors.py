import random
cpu = random.randint(1, 3)

user = input("Enter rock, paper, or scissors: ")

if user == "rock":
	if cpu == 1: # cpu chose rock
		print("Tie game")
	elif cpu == 2: # cpu chose paper
		print("You lost")
	else: # cpu chose scissors
		print("You won!")

elif user == "paper":
	if cpu == 1: # cpu chose rock
		print("You won!")
	elif cpu == 2: # cpu chose paper
		print("Tie game")
	else: # cpu chose scissors
		print("You lost")

else:
	if cpu == 1: # cpu chose rock
		print("You lost")
	elif cpu == 2: # cpu chose paper
		print("You won!")
	else: # cpu chose scissors
		print("Tie game")