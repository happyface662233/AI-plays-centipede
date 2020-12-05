import sys, pygame
from random import randint
from math import trunc
pygame.init()
tilesHeight =100
tilesWide = 100

size = width, height = 600, 600
# win = pygame.display.set_mode((size))

# pygame.display.set_caption("AI Leans Centipede")

def makeGrid():
    pass
def generatePath(x:int ,y:int)->list:#x and y tile not coord
    path = []
    while y >tilesHeight-(trunc(tilesHeight/3)):
        choice=randint(0,3)
        print('looping',choice)
        if choice == 0 and x!= tilesWide:
            print('if 1')
            x+=1
            path.append([x,y])
        elif choice ==1 and x!=0:
            x-=1
            print('if 2')
            path.append([x,y])
        elif choice == 2 and y!=tilesHeight:
            y+=1
            print('if 3')
            path.append([x,y])
        elif choice == 3 and y!=0:
            y-=1 
            print('if 4')
            path.append([x,y])
    return path
print(generatePath(0,0))
        

