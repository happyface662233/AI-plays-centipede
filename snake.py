from random import randint

class snake:
    def __init__(self,x,y,length):
        self.x=x
        self.y=y
        self.length = length
        self.body = self.generateNodePos([1,0])
        self.changeMap = []
    def generateNodePos(self,currentVector:list):
        body = []
        for _ in range(0,self.length):
            body.append({'x':self.x,'y':self.y,'vX':currentVector[0],'vY':currentVector[1]})

        return body
    def move(self):
        for i,piece in enumerate(self.body):
            piece['x'] += piece['vX']
            piece['y'] += piece['vY']
            if 


            