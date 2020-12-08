import sys
import pygame
from random import randint
from math import trunc
import SnakeEnemy 
print(dir(SnakeEnemy))
pygame.init()
tilesHeight = 25
tilesWide = 25

size = width, height = 600, 600
print('HEIGHT ',height,'WIDTH ',width)
win = pygame.display.set_mode((size))

pygame.display.set_caption("AI Leans Centipede")

def notInEmpty(empty,x,y):
    for e in empty:
        if e[0] == x and e[1]==y:
            return True
    return False
def makeGrid(empty:list)->list:
    points =[]

    for x in range(tilesWide):
        for y in range(trunc(tilesHeight*(2/3))):
            c=randint(0,1) 
            if c==0 and notInEmpty(empty,x,y) == False:
                points.append([x,y])
    return points

def generatePath(x: int, y: int) -> list:  # x and y tile not coord
    path = []
    # print(tilesHeight-(trunc(tilesHeight/3)))
    while y < tilesHeight-(trunc(tilesHeight/3)):
        choice = randint(0, 2)
        c2 = randint(0,100)
        # print('looping', choice)
        if choice == 0 and x != tilesWide:
            # print('if 1')
            x += 1
            path.append([x, y])
        elif choice == 1 and x != 0:
            x -= 1
            # print('if 2')
            path.append([x, y])
        elif choice == 2 and y != tilesHeight:
            y += 1
            # print('if 3')
            path.append([x, y])
        if c2<5:
            print('divert')
            path+= generatePath(x,y)

    return path


path1 = generatePath(0, 0)
path2 = generatePath(trunc(tilesWide/2), 0)
print(path2)
s=SnakeEnemy.snakeEnemy(5,5,1,tilesHeight,tilesWide,width,height)
path3 = generatePath(tilesWide, 0)
empty =path1+path2+path3
print(len(path3))
grid = makeGrid(empty)
running = True
while running:
    win.fill((0, 0, 0))
    # path = generatePath(0, 0)
    # for p in path1:
    #     pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
    #         p[0]*(width/tilesWide), p[1]*(height/tilesHeight), width/tilesWide, height/tilesHeight))

    # for p in path2:
    #     pygame.draw.rect(win, (0, 255, 0), pygame.Rect(
    #         p[0]*(width/tilesWide), p[1]*(height/tilesHeight), trunc(width/tilesWide), trunc(height/tilesHeight)))
    #     #print(trunc(width/tilesWide), trunc(height/tilesHeight))
    #     # print(p[0]*(width/tilesWide),p[1]*(height/tilesHeight))

    # for p in path3:
    #     pygame.draw.rect(win, (0, 0, 255), pygame.Rect(
    #         p[0]*(width/tilesWide), p[1]*(height/tilesHeight), width/tilesWide, height/tilesHeight))
    # pygame.display.flip()
    #pygame.display
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            break 
    for space in grid:
        # print(space[0]*(width/tilesWide))
        pygame.draw.rect(win, (0, 0, 255), pygame.Rect(
            space[0]*(width/tilesWide), space[1]*(height/tilesHeight), width/tilesWide, height/tilesHeight))
    s.move(grid)
    win=s.show(win)
    print(s.x,s.y)
    pygame.display.flip()
pygame.quit()
