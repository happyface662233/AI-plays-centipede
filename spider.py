from collections import deque
from random import random


class Spider:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.actions = deque()

    def move(self):
        prob_down = 0.3
        prob_up = 0.3
        prob_right = 1-prob_down-prob_up
        r = random()


if __name__ == '__main__':
    s = Spider(10, 100)
    s.move()
