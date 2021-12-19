from bullet import Bullet
import pygame
from settings import *
import math


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.path = ''
        self.bullets = []
        self.acc = 0

    def moveUp(self):
        self.y -= self.vel

    def moveDown(self):
        self.y += self.vel

    def moveRight(self):
        self.x += self.vel

    def moveLeft(self):
        self.x -= self.vel

    def shoot(self):
        self.bullets.append(Bullet(math.floor(self.x), math.floor(self.y)))

    def update(self, win, ss, grid):

        # print(grid)
        blockCoords = None
        for bullet in self.bullets:
            bullet.move()
            for block in grid:
                if block[0] == bullet.x and block[1] == bullet.y:
                    bullet.alive = False
            win = bullet.show(win)
            if bullet.alive == False:
                self.bullets.remove(bullet)
            res = bullet.isCollided(ss, grid)
            if res[0] == True:
                res2 = bullet.create_two_snakes(ss, res[1], res[2])
                ss += res2['snakes']
                # ss.remove(res[1])
                ss[ss.index(res[1])].dead = True
                ss[ss.index(res[1])].alive = False
                grid.append(res2['blockCoords'])

        return win, ss, grid  # res2['blockCoords']

    def show(self, win):
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(
            self.x*(width/tilesWide), self.y*(height/tilesHeight), width/tilesWide, height/tilesHeight))
        return win
