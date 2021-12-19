from collections import deque
from random import random,randint
import pygame
from settings import *
class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,value):
        self.q.append(value)
    def dequeue(self):
        if len(self.q) !=0:
            x = self.q.pop(0)
            return x
    def peak(self):
        if len(self.q) !=0:
            return self.q[0]
        return None
    def __len__(self):
        return len(self.q)
    

class Spider:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.actions = Queue()
        self.max_height = 5
        self.speed = 1
    def Chose(self):
        move = 0.7
        prob_right = 1-move
        r = random()
        if r <move:
            h = randint(tilesHeight - self.max_height,tilesHeight-1)
            self.actions.enqueue({
                'x':self.x,
                'y':h
            })
        else:
            self.actions.enqueue({
                'x':self.x+1,
                'y':self.y
            })
    def Move(self):
        #print(len(self.actions))
        
        if len(self.actions)==0:
            self.Chose()
        else:
            #print(self.actions.peak())
            if self.x-self.actions.peak()['x'] == 0 and self.y-self.actions.peak()['y'] == 0:
                self.actions.dequeue()
                self.Chose()
            else:
                if self.actions.peak()['x'] != self.x:
                    self.x = self.actions.dequeue()['x']
                elif self.actions.peak()['y'] != self.y:
                    #self.x = self.actions.peak()['x'].dequeue()
                    if self.actions.peak()['y']-self.y <0:
                        self.y-=self.speed
                    else:
                        self.y+=self.speed
        if self.x>tilesWide:
            self.x= -1
    def isHittingPlayer(self,p):
        if p.x== self.x and p.y== self.y:
            return True
        return False
    def show(self, win):
        pygame.draw.rect(win, (255, 255, 0), pygame.Rect(
            self.x*(width/tilesWide), self.y*(height/tilesHeight), width/tilesWide, height/tilesHeight))
        return win



if __name__ == '__main__':
    s = Spider(10, 100)
    s.Move()
