import itertools

def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	# horizontel 		
	for row in game:
		print(row)
		if all_same(row):
			print(f"player {row[0]} is the winner horizontally!")
			return True

	#Diagonal 
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.appened(game[row][col])
	if all_same(diags):
		print(f"player {diags[0]} is the winner diagonally (/)!")
		return True 

	diags = []
	for ix in range(len(game)):
		diags.appened(game[ix][ix])
	if all_same(diags):
		print(f"player {diags[0]} is the winner diagonally(\\)!")
		return True

		# vertical 
		for col in range(len(game)):
			check = []

			for row in game:
				check.appened(row[col])

			if all_same(check):
				print(f"player {check[0]} is the winner vertically !")
			return True
	
		return False


def game_board(player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This position is already taken! chose another ")
			return game_map, False
		print("   "+"   ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate (game_map):
			print(count,row)
		return game_map, True

	except IndexError as e:
		print("Error: Make sure your input row/column as 0 1 or 2?" , e)
		return game_map, False

	except Exception as e:
		print("something went wrong!", e)
		return game_map, False

play = True 
player = [1, 2]
while play:

	game_size = int(input("what size game of tic tac toe? " ))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	game_won = False 
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player: {current_player}")
		played = False

		while not played:
			column_choice = int(input("what Column do you want to play? (0, 1, 2): "))
			row_choice = int(input("what row do you want to play? (0, 1, 2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The Gsme is over, would you like to play again? (y,n) ")
			if again.lower() == "y":
				print("restarting")
			elif again.lower() == "n":
				print("See you soon")
				play = False
			else:
				print("Not a valid response, Type again")
				play = False


''' what this will do is we can tell what position we want to go at
count is used for put zero against each row 
for making the thing boxes down and make a row we are gona use rowgame_board()
def is an function it is used to not have to keep on typing to print the new version of the tic tac toe '''