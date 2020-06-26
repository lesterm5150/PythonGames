import pygame
import random
import sys
import math
from copy import copy,deepcopy
from pygame.locals import *
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
    else:return False

def die(screen, score):
    f=pygame.font.SysFont('Arial', 30);
    t=f.render('Your score was: '+str(score), True, (0, 0, 0));
    screen.blit(t, (10, 270));
    pygame.display.update();
    pygame.time.wait(2000);
    sys.exit(0)

def pathFound(grid,xApple,yApple,snake):
# if apple directly behind it
# If apple appears close to its body
    gridTmp = deepcopy(grid)
    snakeBod= deepcopy(snake)
    #grid = grid1
    direct=[]
    walls=[]
    noBack = False
    timeout=0
    xHead = 0
    yHead = 0
    ##TURN THE SNAKE AROUND
    xHead,yHead = snakeBod[0]
    inside = False
    snakeBodLen = len(snake)
    while(xHead != xApple or yHead != yApple):
        xd = xApple-xHead
        yd = yApple-yHead
        for k in range(0 ,snakeBodLen-1):
            x,y = snakeBod[k]
            if(k==0):
                gridTmp[x][y] = 4
            else:
                gridTmp[x][y] = 3
            
        if(yd>0 and 0<= yHead <=29 and gridTmp[xHead][yHead+1] <3) : #Go down
            direct.append(0)
            snakeBod.insert(0,(xHead,yHead+1))
            for x,y in walls:
                grid[x][y] = 0
            walls = []
            
        elif(xd>0 and 0<= xHead <=29 and gridTmp[xHead+1][yHead] <3) : #Go right
            direct.append(1)
            snakeBod.insert(0,(xHead+1,yHead))
            for x,y in walls:
                grid[x][y] = 0
            walls = []

        elif(yd<0 and 0<= yHead <=29 and gridTmp[xHead][yHead-1] <3): #Go up
            direct.append(2)
            snakeBod.insert(0,(xHead,yHead-1))
            for x,y in walls:
                grid[x][y] = 0
            walls = []

        elif(xd<0 and 0<= xHead <=29 and gridTmp[xHead-1][yHead] <3): #Go left
            direct.append(3)
            snakeBod.insert(0,(xHead-1,yHead))
            for x,y in walls:
                grid[x][y] = 0
            walls = []
            
        elif((0<= yHead <=29 and 0<= xHead <=29)):
            if(gridTmp[xHead][yHead-1] <3 ): #Go up
                direct.append(2)
                snakeBod.insert(0,(xHead,yHead-1))
                for x,y in walls:
                    grid[x][y] = 0
                walls = []

                
            elif(gridTmp[xHead][yHead+1] <3) : #Go down
                direct.append(0)
                snakeBod.insert(0,(xHead,yHead+1))
                for x,y in walls:
                    grid[x][y] = 0
                walls = []

            
            elif(gridTmp[xHead+1][yHead] <3 ) : #Go right
                direct.append(1)
                snakeBod.insert(0,(xHead+1,yHead))
                for x,y in walls:
                    grid[x][y] = 0
                walls = []

                
            elif(gridTmp[xHead-1][yHead] <3 ): #Go left
                direct.append(3)
                snakeBod.insert(0,(xHead-1,yHead))
                for x,y in walls:
                    grid[x][y] = 0
                walls = []
                  

            else:            
                #print(len(snakeBod))
                #print(str(snakeBodLen))
                #for j in range (0,len(gridTmp)-1):
                    #print(gridTmp[j])
                #print("POPPED")
                if(len(direct)> 0):                
                    direct.pop()
                    x,y = snakeBod.pop(0)
                    gridTmp[x][y]=5
                    walls.append((x,y))
                else:
                    print(len(snakeBod))
                    print(str(snakeBodLen))
                    for j in range (0,len(gridTmp)-1):
                        print(gridTmp[j])
                    sys.exit()

        else:            
            if(len(direct)> 0):                
                direct.pop()
                x,y = snakeBod.pop(0)
                gridTmp[x][y]=5
                walls.append((x,y))
            else:
                print(len(snakeBod))
                print(str(snakeBodLen))
                for j in range (0,len(gridTmp)-1):
                    print(gridTmp[j])
                sys.exit()
        
        #getting the snake
        for k in range(0,snakeBodLen):
            x,y = snakeBod[k]
            gridTmp[x][y] = 0
        #gridTmp = deepcopy(grid)
        xHead,yHead = snakeBod[0]
##        for k in range(1,snakeBodLen-2):
##            snakeBod[k]=snakeBod[k+1]

        

    
    
    
    return direct


    

def findDir(xs,ys,applePos,dirs,i,grid, snake):

#0 is down
#1 is right
#2 is up
#3 is left
#x is keft right


    xApple = int(round(applePos[0]/20))
    yApple = int(round(applePos[1]/20))
    #print("Appx : " + str(xApple) + " Appy : " + str(yApple))
    grid[xApple][yApple] = 1



    moves=[]


    moves=(pathFound(grid,xApple,yApple,snake))
    grid[xApple][yApple] = 0
    return moves



#fix apple so it can't apear in the snake
xs = [280, 290, 290, 290, 290];
ys = [280, 260, 240, 220, 200];
dirs = 0;
score = 0;
applepos = (random.randint(0, 580), random.randint(0, 580));
pygame.init();
s=pygame.display.set_mode((600, 600));
pygame.display.set_caption('Snake');
appleimage = pygame.Surface((10, 10));
appleimage.fill((0, 255, 0));
headImg = pygame.Surface((20,20))
headImg.fill((0,0,255))
img = pygame.Surface((20, 20));
img.fill((255, 0, 0));
f = pygame.font.SysFont('Arial', 20);
clock = pygame.time.Clock()

grid = [[0 for x in range(31)] for x in range(31)]
for i in range(0,31):
    for j in range(0,31):
        grid[i][j] = 0
moves = []
snake =[]

while True:
    clock.tick(50)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
        elif e.type == KEYDOWN:
            if e.key == K_UP and dirs != 0:
                dirs = 2
            elif e.key == K_DOWN and dirs != 2:
                dirs = 0
            elif e.key == K_LEFT and dirs != 1:
                dirs = 3
            elif e.key == K_RIGHT and dirs != 3:
                dirs = 1
    i = len(xs)-1
    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
            die(s, score)
        i-= 1
    if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 20, 20, 20):
        score+=1;
        #expand the snake
        xs.append(xs[len(xs)-1]);
        ys.append(ys[len(ys)-1]);
        #generates new apple
        appleInSnake = True
        j=0
        while True:
            applepos=(random.randint(0,580),random.randint(0,580))
            for i in range (0,len(xs)):
                if(collide(xs[i], applepos[0], ys[i], applepos[1], 30, 30, 30, 30)):
                    break
                else:
                    if i == len(xs)-1:
                        j=-2
                        break
            if j==-2 :
                break
        #xs is x direction minus is left
    #ys is y direction minus is up
    #goes from 0 to 580 in square
    #apple pos is where apple is
    if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
        die(s, score)
    i = len(xs)-1


    #print ("Direction -> " +str(moves))
    if(len(moves)==0):
        snake = []
        for i in range(0,len(xs)):
             snake.append((int(xs[i]/20),int(ys[i]/20)))
        moves=findDir(xs,ys,applepos,dirs,i,grid,snake)
    if(len(moves)>0):
        dirs=moves[0]
        moves.pop(0)


    #print ("Direction -> " +str(dirs))



    while i >= 1:
        xs[i] = xs[i-1];
        ys[i] = ys[i-1];
        i -= 1

    if dirs==0:
        ys[0] += 20 #down
    elif dirs==1:
        xs[0] += 20 #right
    elif dirs==2:
        ys[0] -= 20 #up
    elif dirs==3:
        xs[0] -= 20 #left
    #Updates the map

    s.fill((255, 255, 255))
    s.blit(headImg,(xs[0],ys[0]))
    for i in range(1, len(xs)):
        s.blit(img, (xs[i], ys[i]))
    #blitt shows an image
    s.blit(appleimage, applepos);
    t=f.render(str(score), True, (0, 0, 0));
    s.blit(t, (10, 10));
    pygame.display.update()





