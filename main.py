from random import randrange, choice
from classes import *
from functions import *
from argparse import ArgumentParser
from logging import basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL

# tuple | 2(c)
letters = tuple("WASDRQUVwasdrquv")
actions = ("Up", "Left", "Down", "Right", "Restart", "Quit", "Undo", "Save")

# dict | 2(a)
actions_dict = dict(zip(letters, actions * 2))

#global variable game | 1(a)(i)
game = None

# play() is a recursive function calls itself | 1(f)(iii)
def play():
	global game
	draw_field = display(game.height, game.width)
	draw_field(game.gameboard.field)
	if((not game.is_win()) and (not game.is_lose())):
		print("Your current score is " + str(game.score))
		letter = input("input direction: UP(w),Down(s),Right(d),Left(a),Restart(r),Quit(q),Undo(u),Save and quit(v): ")
		if(letter in letters[:]):
			if(actions_dict[letter] == "Restart"):
				# a function that changes the global variable "game" | 1(f)(vi)
				game = newGame()
				play()
			elif(actions_dict[letter] == "Quit"):
				exit(0)
			elif(actions_dict[letter] == "Undo"):
				game.undo()
				play()
			elif(actions_dict[letter] == "Save"):
				game.save()
				exit(0)
			# actions[0 : 4] ranged slicing of a tuple | 2(f)
			elif(actions_dict[letter] in actions[0 : 4]):
				game.move(actions_dict[letter])
				play()
		else:
			play()
	else:
		if(game.is_win()):
			print("Wow, you win! Your score is: " + str(game.score))
		else:
			print("Sorry, you lost! Your score is: " + str(game.score))
		again = input("Would you want to play the game again(y for Yes, otherwise No)?")
		if again in tuple("Yy"):
			game = newGame()
			play()
		else:
			exit(-1)

def main(loadgame):
	global game
	if(loadgame):
		game = Game()
	else:
		game = newGame()
	play()




if __name__ == "__main__":
	parser = ArgumentParser(description = "A more complicated 2048 game" +
					  "with optional options")
	# This is a mandatory command line option | 1(i)(i)
	parser.add_argument("name", help = "Player's name")

	# This is an optional command line option | 1(i)(ii)
	parser.add_argument("-l", "--loadgame", help = "load game or not, a boolean value",
				action = "store_true")

	parse_result = parser.parse_args()
	print("Hello " + parse_result.name + ", this is a 2048 game.")
	

	# logging | 2(l)
	reset_settings()
	basicConfig(filename = "log", level = CRITICAL, \
		    format = parse_result.name + " start the game at %(asctime)s")
	write_logs()

	main(parse_result.loadgame)