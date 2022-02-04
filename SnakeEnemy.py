from random import randint
import pygame
from time import sleep
from settings import *
import os
# from gameScreen import tilesHeight,tilesWide,width,height


class snakeEnemy:
    def __init__(self, x, y, length):
        image = pygame.image.load(os.path.join('assets', 'body.png'))
        self.image = pygame.transform.scale(image, (width//tilesWide, height//tilesHeight))
        # global tilesWide,tilesHeight,width,height
        #self.default_speed_component = 0.2
        self.default_speed_component = 1

        self.x = x
        self.y = y
        self.length = length
        self.body = self.createBody([self.default_speed_component, 0])
        self.changeMap = []
        self.grid = []
        self.dead = False
        self.frames = 0

        # print('MAKING')

    def createBody(self, currentVector: list):
        body = []
        for i in range(0, self.length):
            body.append({'x': self.x, 'y': self.y-i,
                         'vX': currentVector[0], 'vY': currentVector[1]})

        return body

    # def move(self, grid):
    #     for i, piece in enumerate(self.body):
    #         piece['x'] += piece['vX']
    #         piece['y'] += piece['vY']
    #         for g in grid:
    #             if piece['x'] == g[0] and piece['y'] == g[1]:
    #                 print('selcted')
    #                 self.changeMap.append(
    #                     [piece['x'], piece['y'], piece['vX']*-1, -1])
    #                 piece['x'] -= piece['vX']
    #                 self.changeMap.append(
    #                     [piece['x'], piece['y']-1, piece['vX'], 0])
    #         for change in self.changeMap:

    #             if change[0] == piece['x'] and change[1] == piece['y']:
    #                 piece['vX'] = change[2]
    #                 piece['yX'] = change[3]
    def move(self):

        for i, b in enumerate(self.body):
            if b['x'] < 0:
                print('big error here')
            if b['y'] < 0:
                #print('I AM BELLOW ONE ', self.body[i]['y'])
                self.body[i]['y'] += 1
                #print('I AM ABOVE ONE ', self.body[i]['y'])

            else:
                self.body[i]['x'] += b['vX']
                for g in self.grid:
                    # print('GGGGGGG: ', g)
                    # print(b, g)
                    if i == 0 or i == len(self.body)-1:

                        if (g[0] == round(b['x'])) and (g[1] == round(b['y'])):

                            self.bounce(i)
                            # if i == len(self.body)-1:
                            #     # print('bouncing')
                            break
                        elif round(b['x']) <= 0 or round(b['x']) == tilesWide:

                            self.bounce(i)
                    else:
                        for c in self.changeMap:
                            if b['x'] == c[0] and b['y'] == c[1]:
                                # print(
                                #     'I AM NOT THE LEADER BUT I AM BOUNCING ', b, c)
                                self.bounce(i)
            self.frames += 1

    def bounce(self, i):
        # print('bounce')
        self.body[i]['vX'] *= -1
        self.body[i]['y'] += 1
        self.body[i]['x'] += self.body[i]['vX']
        self.changeMap.append(
            [self.body[i]['x']-self.body[i]['vX'], self.body[i]['y']-1])

    def show(self, win):
        for piece in self.body:
            # pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
            #     100, 100, 100, 100))
            #print('MESSED UP BODY ', piece)
            # pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
            #     piece['x']*(width/tilesWide), piece['y']*(height/tilesHeight), width/tilesWide, height/tilesHeight))
            win.blit(self.image,(piece['x']*(width/tilesWide), piece['y']*(height/tilesHeight), width/tilesWide, height/tilesHeight))
            # print('PIECE ', piece['x'], piece['y'])
        return win
