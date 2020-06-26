import pygame
import random
import sys
import math
from pygame.locals import *

gridSize = 10
letters = ['A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H' ,'I','J']

class Grid():
    def __init__(self):

        self.size = gridSize
        self.pieces = []
        self.grid = self.gridMe()
        self.coord = []
        a = aircraftCarrier()
        b = battleShip()
        c = Submarine()
        d = Cruiser()
        e = Destroyer()
        self.pieces.append(a)
        self.pieces.append(b)
        self.pieces.append(c)
        self.pieces.append(d)
        self.pieces.append(e)
        self.playerNumber = 0
        self.getPieces()

    def gridMe(self):
        grid = [[0 for x in range(self.size)] for x in range(self.size)]
        for i in range(0,self.size):
            for j in range(0,self.size):
                grid[i][j] = 0
        return grid
    
    def getPieces(self):
        self.displayGrid()
        
        for p in self.pieces:
            go = True
            while(go == True):
                head = input("Please choose where the head of the "+ p.name +" will be? (letter first)\n")
                p.alignment = int(input("1) Vertical\n2) Horizontal\n"))
               
                a = str(head[0])
                b = int(head[1])
               
                b = b-1
                c = letters.index(a)
                if (c,b) not in self.coord:
                    self.coord.append((c,b))
                    go = False
                else:
                    print("Not a valid placement, please try again")
                   
                p.head.append((c,b))
                p.fillPiece()
        

    def displayGrid(self):
        print('   1  2  3  4  5  6  7  8  9  10')
        j=0
        for i in self.grid:
            print(letters[j] + ' ' + str(i))
            j+= 1
        
##        self.grid = self.lockGrid()

##    def lockGrid(self):
##        grid = [[0 for x in range(self.size)] for x in range(self.size)]
##        for i in range(0,self.size):
##            for j in range(0,self.size):
##                grid[i][j] = 0
##        for x,y in self.teamA:
##            grid[x][y] = 3 # 3 is where a ship is
##        return grid


    
class Piece():
    def __init__(self):
        self.positions = []
        self.head = []
        self.alignment = 0
        self.placed = False
        self.destroyed = False
        
        
    def fillPiece(self):
        x,y = self.head[0]
        for i in range(0,self.size):
            if self.alignment == 1:
                self.positions.append((x,y+i))
            else:
                self.positions.append((x+i,y))
            

class aircraftCarrier(Piece):
    def __init__(self):
        super(aircraftCarrier, self).__init__()
        self.size = 5
        self.name = 'Aircraft Carrier'
        self.color = [255,0,0]
        

class battleShip(Piece):
    def __init__(self):
        super(battleShip, self).__init__()
        self.size = 4
        self.name = 'Battleship'
        self.color = [200,50,50]

class Submarine(Piece):
    def __init__(self):
        super(Submarine, self).__init__()
        self.size = 3
        self.name = 'Submarine'
        self.color = [50,200,50]

class Cruiser(Piece):
    def __init__(self):
        super(Cruiser, self).__init__()
        self.size = 3
        self.name = 'Cruiser'
        self.color = [50,100,0]

class Destroyer(Piece):
    def __init__(self):
        super(Destroyer, self).__init__()
        self.size = 2
        self.name = 'Destroyer'
        self.color = [50,50,50]


    



player1Grid = Grid()
player1Grid.playerNumber=1
for piece in player1Grid.pieces:
    print(piece.positions)

player2Grid = Grid()
player2Grid.playerNumber=1

##a = ((1,2),(3,4))
##b = ((4,5),(6,2))
##grid = Grid(a,b)


##choose = int(input("1 ) 2 Player\n2) Against Cpu\n"))
##if choose == 1:
##elif choose == 2:
##else :
##    print("Sorry that wasn't a choice")
##    sys.exit()
