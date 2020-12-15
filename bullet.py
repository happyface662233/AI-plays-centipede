import pygame
from settings import *


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = -1
        self.alive = True
    def move(self):
        self.x += self.velX
        self.y += self.velY

    def isCollided(self, snake, grid):
        for piece in snake.body:
            if piece['x'] == self.x and piece['y'] == self.y:
                print('bullet hit the snake')
                self.alive = False
    

    def show(self, win):
        pygame.draw.rect(win, (255, 0, 255), pygame.Rect(
            self.x*(width/tilesWide), self.y*(height/tilesHeight), width/tilesWide, height/tilesHeight))
        return win


'''            
pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
                piece['x']*(self.width/self.tilesWide), piece['y']*(self.height/self.tilesHeight), self.width/self.tilesWide, self.height/self.tilesHeight))
                '''
