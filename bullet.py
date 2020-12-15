import pygame
from settings import *
from SnakeEnemy import snakeEnemy


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
                if piece['x'] == self.x and piece['y'] == self.y:
                    print('NORMAL SNAKE BODY', snakes[0].body)
                    print('bullet hit the snake')
                    self.alive = False
                    snake.end = True
                    snakeBody1 = snake.body[:i]
                    print('SNAKE BODY 1', snakeBody1)
                    snakeBody2 = snake.body[i:]
                    if piece['vX'] == -1:
                        # snake 2 should go the opposite way
                        #snakeBody1_ = [i['vX']*-1 for i in snakeBody1]
                        snakeBody1_ = []
                        for i in snakeBody1:
                            i['vX'] *= -1
                            snakeBody1_.append(i)

                        snake1 = snakeEnemy(
                            snake.body[-1]['x'], snake.body[-1]['y'], 0)
                        snake1.body = snakeBody1_
                        snake2 = snakeEnemy(
                            snake.body[0]['x'], snake.body[0]['y'], 0)
                        snake2.body = snakeBody2
                    else:
                        #snakeBody2_ = [i['vX'] * -1 for i in snakeBody2]
                        snakeBody2_ = []
                        for i in snakeBody2:
                            i['vX'] *= -1
                            snakeBody2_.append(i)
                        snake2 = snakeEnemy(
                            snake.body[-1]['x'], snake.body[-1]['y'], 0)
                        snake2.body = snakeBody2_
                        snake1 = snakeEnemy(
                            snake.body[0]['x'], snake.body[0]['y'], 0)
                        snake1.body = snakeBody1
                    newSnakes.append(snake1)
                    newSnakes.append(snake2)
                    print(newSnakes)
        return newSnakes

    def show(self, win):
        pygame.draw.rect(win, (255, 0, 255), pygame.Rect(
            self.x*(width/tilesWide), self.y*(height/tilesHeight), width/tilesWide, height/tilesHeight))
        return win


'''            
pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
                piece['x']*(self.width/self.tilesWide), piece['y']*(self.height/self.tilesHeight), self.width/self.tilesWide, self.height/self.tilesHeight))
                '''
