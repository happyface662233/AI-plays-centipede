import pygame
from settings import *
from SnakeEnemy import snakeEnemy
import math


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

    def isCollided(self, snakes, grid):
        newSnakes = []
        for snake in snakes:
            for i, piece in enumerate(snake.body):
                print(
                    f"snake body = [{piece['x']}, {piece['y']}], {self.x}, {self.y}")
                # if piece['x']-1 > self.x > piece['x']+1 and round(piece['y']) == round(self.y):
                if self.x-1 < piece['x'] < self.x+1 and self.y-1 < piece['y'] < self.y+1:
                    print('hit')
                    return (True, snake, piece)
        return [False, None, None]

    def create_two_snakes(self, snakes, snake, piece):
        index = snakes.index(snake)
        hit_snake = snakes[index]

        piece_index = snake.body.index(piece)
        # b,b,b,#b,b,b,b
        # attrs dont matter well overwrite them in a min
        if len(hit_snake.body) == 1:
            return{'snakes': [], 'blockCoords': [round(piece['x']), round(piece['y'])]}

        s1 = snakeEnemy(0, 0, 1)
        s1.body = snake.body[:piece_index]
        s2 = snakeEnemy(0, 0, 1)
        s2.body = snake.body[piece_index+1:]
        s1.changeMap = snake.changeMap
        s2.changeMap = snake.changeMap

        # if hit_snake.body[0]['vX'] > 0:
        #     s1.bounce(-1)
        return {'snakes': [s1, s2], 'blockCoords': [round(piece['x']), round(piece['y'])]}

    def show(self, win):
        pygame.draw.rect(win, (255, 0, 255), pygame.Rect(
            round(self.x)*(width/tilesWide), round(self.y)*(height/tilesHeight), width/tilesWide, height/tilesHeight))
        return win


'''
pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
                piece['x']*(self.width/self.tilesWide), piece['y']*(self.height/self.tilesHeight), self.width/self.tilesWide, self.height/self.tilesHeight))
                '''
