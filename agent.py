import player
import cv2 
import numpy as np
class Agent(player.player):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.actions =[self.moveUp, self.moveDown, self.moveLeft, self.moveRight]
        self.table =[] #{'env':reward}

        #same nn for stability
        self.running =None
        self.training =None
    def collectFrame(self,env,reward):
        self.table.append({env:reward})
    def forProcessing(self,screen,reward):
        pass
