from random import randint
import pygame
#from gameScreen import tilesHeight,tilesWide,width,height
class snakeEnemy:
    def __init__(self,x,y,length,tilesHeight,tilesWide,width,height):
        #global tilesWide,tilesHeight,width,height
        self.tilesHeight = tilesHeight
        self.tilesWide = tilesWide
        self.width = width
        self.height = height
        self.x=x
        self.y=y
        self.length = length
        self.body = self.createBody([1,0])
        self.changeMap = []
    def createBody(self,currentVector:list):
        body = []
        for _ in range(0,self.length):
            body.append({'x':self.x,'y':self.y,'vX':currentVector[0],'vY':currentVector[1]})

        return body
    def move(self,grid):
        for i,piece in enumerate(self.body):
            piece['x'] += piece['vX']
            piece['y'] += piece['vY']
            for g in grid:
                if piece['x'] == g[0] and piece['y'] == g[1]:
                    self.changeMap.append([piece['x'],piece['y'],piece['vX']*-1,-1])
                    piece['x']-=piece['vX']
                    self.changeMap.append([piece['x'],piece['y']-1,piece['vX'],0])
            for change in self.changeMap:
                if change[0] == piece['x'] and change[1] == piece['y']:
                    piece['vX'] = change[2]
                    piece['yX'] = change[3] 
    def show(self,win):
        for piece in self.body:
            pygame.draw.rect(win, (0, 0, 255), pygame.Rect(
                piece['x']*(self.width/self.tilesWide), piece['y']*(self.height/self.tilesHeight), self.width/self.tilesWide, self.height/self.tilesHeight))
        return win
            


            