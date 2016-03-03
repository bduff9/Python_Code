from PIL import Image

from drawing import *

from image_display import *

from random import *

def createBoard(cells):

    board = []

    for i in range(cells[0]):

        column = []
	
        for i in range(cells[1]):

            column.append(0)
            
        board.append(column)
	
    return board
    
def drawBoard(board, cellsize):

    cells = (len(board),len(board[0]))
    w=cells[0]*cellsize
    h=cells[1]*cellsize
    img=Image.new('RGB',(w,h), (255,255,255))

    for col in range(len(board)):
        for row in range(len(board[col])):
            if(board[col][row]==1):
                for i in range(col*cellsize,cellsize*(col+1)):
                    for j in range(row*cellsize,cellsize*(row+1)):
                        img.putpixel((i,j),(0,0,0))
                
    for x in range(0,w,cellsize):
        for y in range(0,h,cellsize):
            drawLine(img,(x,y),(w-1,y),(0,0,0))
    
    for y in range(0,h,cellsize):
        for x in range(0,w,cellsize):
            drawLine(img,(x,y),(x,h-1),(0,0,0))
    
    return img
    
def countNeighbors(board, location):

    col,row=location
    num=0
    
    if(col-1>=0 and row-1>=0):
        if(board[col-1][row-1]==1):
            num+=1
    if(col>=0 and row-1>=0):
        if(board[col][row-1]==1):
            num+=1
    if(col+1>=0 and row-1>=0):
        if(board[col+1][row-1]==1):
            num+=1
    if(col-1>=0 and row>=0):
        if(board[col-1][row]==1):
            num+=1
    if(col+1>=0 and row>=0):
        if(board[col+1][row]==1):
            num+=1
    if(col-1>=0 and row+1>=0):
        if(board[col-1][row+1]==1):
            num+=1
    if(col>=0 and row+1>=0):
        if(board[col][row+1]==1):
            num+=1
    if(col+1>=0 and row+1>=0):
        if(board[col+1][row+1]==1):
            num+=1
        
    return num
    
def checkIfLiving(board, location, rules):
    
    life = 0
    num = countNeighbors(board,location)
    
    for x in rules:
        if(x==num):
            life=1
            
    return life
    
def processBoard(board, born_rules, survive_rules):
	
newBoard=board.copy()
for x in range(len(board)):
	for y in range(len(board[x])):
		if(board[x][y]==1):
			if(checkIfLiving(board,(x,y),survive_rules)==0):
				newBoard[x][y]=0
		else:
			if(checkIfLiving(board,(x,y),born_rules)==1):
				newBoard[x][y]=1

    return newBoard
    
def gameofLife(frames=100, cellsize=10, initial_board=None, born_rules=[3], survive_rules=[2,3]):
	lifeMovie=[]
	if(initial_board=None):
		initial_board=createBoard((50,50))
		addRandomFill(initial_board,(0,0),(49,49),.5)

	lifeMovie.append(drawBoard(initial_board,cellsize))
	for x in range(frames):
		initial_board=processBoard(initial_board,born_rules,survive_rules)
		lifeMovie.append(drawBoard(initial_board,cellsize))

    return lifeMovie
    
def addBox(board,location):
    
    col,row=location
    if(col+1<len(board) and row+1<len(board[0])):
        board[col][row]=1
        board[col][row+1]=1
        board[col+1][row]=1
        board[col+1][row+1]=1
    
def addBlinker(board,location,orientation):

    col,row=location
    if(orientation):
        if(row+2<len(board[0])):
            board[col][row]=1
            board[col][row+1]=1
            board[col][row+2]=1
    else:
        if(col+2<len(board)):
            board[col][row]=1
            board[col+1][row]=1
            board[col+2][row]=1
    
def addGlider(board,location):

     col,row=location
    if(col+2<len(board) and row+2<len(board[0])):
        board[col][row]=1
        board[col][row+1]=1
        board[col][row+2]=1
        board[col+1][row]=1
	board[col+2][row+1]=1
    
def addRandomFill(board,location1,location2,threshold):
	
	w,h=len(board),len(board[0])

    if(location1[0]>=0 and location1[1]>=0):
	if(location2[0]<w and location2[1]<h):
		for x in range(location2[0]):
			for u in range(location2[1]):
				if(random.random()<threshold):
					board[x][y]=1
    
def addList(board,cells):

    w,h=len(board),len(board[0])
	for x in range(len(cells)):
		if(cells[x][0]<w and cells[x][1]<h):
			board[cells[x][0]][cells[x][1]]=1

board = createBoard((20,15))

addBox(board,(3,3))

addBox(board,(5,10))

addBlinker(board, (13,2), True)

addBlinker(board, (10,7), False)

im = drawBoard(board,15)
print checkIfLiving(board,(3,3),(1,2))
im.show()

'''
board = createBoard((10,10))
board[3][7]=1
board[5][8]=1
print board
img = drawBoard(board, 50)
img.show()
'''
