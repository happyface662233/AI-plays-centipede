from bullet import Bullet
import pygame
from settings import *


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.path = ''
        self.bullets = []

    def moveUp(self):
        self.y -= self.vel

    def moveDown(self):
        self.y += self.vel

    def moveRight(self):
        self.x += self.vel

    def moveLeft(self):
        self.x -= self.vel

    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y))

    def update(self, win,s,grid):
        for bullet in self.bullets:
            bullet.move()
            win = bullet.show(win)
            if bullet.alive == False:
                self.bullets.remove(bullet)
            bullet.isCollided(s,grid)
        return win

    def show(self, win):
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(
            self.x*(width/tilesWide), self.y*(height/tilesHeight), width/tilesWide, height/tilesHeight))
        return win
