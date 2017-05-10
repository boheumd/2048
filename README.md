# 2048
My 2048 game

User manual:
	Command line:
		A mandatory command line option: your name
		An optional command line option: Choose whether to continue the saved game or not. -l means to continue. Without -l, play a new game.

Input before game :
	Before the game, you will be asked to input the height and the width of the chessboard and the default value of these two number is 4. Also, you will be asked to input the target of this game. The default value of target is 2048.

Input during game:
	During the game, you can choose one from the four directions(Up, Left, Down, Right). You also can restart the game, quit the game. This game also supports “undo” function, you can undo for one step. You can choose to save the game and quit. Then you can continue on your saved game later.

log:
	This is the log file records the time of entering the game and corresponding player’s name.

save.json:
	This is the json file that contains all the information of the saved game.

Reproducible use cases that cover all features:
	Command line: python3 main.py player (-l)
	Input height: 4
	Input width: 4
	Target : 256
	Then you can just play the game according to the prompt until you lose the game or win the game.
