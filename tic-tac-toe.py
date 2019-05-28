board=[["_",'_','_'],["_",'_','_'],["_",'_','_']]

def display_board():
	for i in board:
		print(' '.join(i))
	print()
	print()
comp='O'
player='X'
def edit_board(row , col,ch ):
	board[row][col]=ch

def is_empty():
	for i in board:
		for j in i:
			if j =='_':
				return True
	return False
def score(depth):
	for i in range(3):
		if (board[i][0]==board[i][1]) and (board[i][2]==board[i][0]):
			if board[i][0]=='O':
				return 20-depth
			elif board[i][0]=='X':
				return depth-20
	for i in range(3):
		if (board[0][i]==board[1][i]) and (board[2][i]==board[0][i]):
			if board[0][i]=='O':
				return 20-depth
			elif board[0][i]=='X':
				return depth-20
	if (board[1][1]==board[2][2]) and (board[2][2]==board[0][0]):
		if board[0][0]=='O':
			return 20-depth
		elif board[0][0]=='X':
			return depth-20
	if (board[0][2]==board[1][1]) and (board[1][1]==board[2][0]):
		if board[1][1]=='O':
			return 20-depth
		elif board[1][1]=='X':
			return depth-20
	return 0


def max_(depth):
	if not is_empty():
		return 0
	temp = score(depth)
	if temp == 20-depth or temp==depth-20:
		return temp
	maxi=-10000000
	for i in range(3):
		for j in range(3):
			if board[i][j]=='_':
				board[i][j]=comp
				score1 = min_(depth+1)
				if score1>maxi:
					maxi= score1
				board[i][j]='_'
	return maxi
def min_(depth):
	if not is_empty():
		return 0
	temp = score(depth)
	if temp == 20-depth or temp==depth-20:
		return temp
	mini=10000000
	for i in range(3):
		for j in range(3):
			if board[i][j]=='_':
				board[i][j]=player
				score1= max_(depth+1)
				if score1<mini:
					mini= score1
				board[i][j]='_'
	return mini
def best_move(depth):
	row,col=-1,-1
	best=-100000
	for i in range(3):
		for j in range(3):
			if board[i][j]=="_":
				board[i][j]=comp
				score1 = min_(depth+1)
				if score1>best:
					best=score1
					row,col=i,j
				board[i][j]="_"
	return row,col
def game():
	player='X'
	comp='O'
	move=[]
	depth=1
	display_board()
	while( is_empty()):

		print("Enter the row and column")
		row,col=map(int ,input().split())
		edit_board(row,col,player)
		display_board()
		score1= score(depth)
		if score1==depth-20:
			print("YOU WON, YOU are LUCkY today , try your luck on a lottery ticket")
			break
		depth = depth +1
		row,col = best_move(depth)
		edit_board(row,col,comp)
		display_board()
		point = score(depth)
		if point== 20-depth:
			print("YOU LOST")
			break
	print("DRAW")

game()




 

 



