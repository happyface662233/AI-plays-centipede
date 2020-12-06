import sys
import pygame
from random import randint
from math import trunc
pygame.init()
tilesHeight = 25
tilesWide = 25

size = width, height = 600, 600
win = pygame.display.set_mode((size))

pygame.display.set_caption("AI Leans Centipede")


def makeGrid():
    pass


def generatePath(x: int, y: int) -> list:  # x and y tile not coord
    path = []
    # print(tilesHeight-(trunc(tilesHeight/3)))
    while y < tilesHeight-(trunc(tilesHeight/3)):
        choice = randint(0, 2)
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

    return path


path1 = generatePath(0, 0)
path2 = generatePath(trunc(width/2), 0)
print(path2)
path3 = generatePath(width, 0)
print(len(path3))
while True:
    win.fill((0, 0, 0))
    # path = generatePath(0, 0)
    # for p in path1:
    #     pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
    #         p[0]*(width/tilesWide), p[1]*(height/tilesHeight), width/tilesWide, height/tilesHeight))

    for p in path2:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(
            p[0]*(width/tilesWide), p[1]*(height/tilesHeight), width/tilesWide, height/tilesHeight))

    for p in path3:
        pygame.draw.rect(win, (0, 0, 255), pygame.Rect(
            p[0]*(width/tilesWide), p[1]*(height/tilesHeight), width/tilesWide, height/tilesHeight))
    pygame.display.flip()
    pygame.display
pygame.quit()
