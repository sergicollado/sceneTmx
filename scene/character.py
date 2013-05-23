from helpers import *

class Character:
    def __init__(self):
        self.position = Position(0,0)
        self.speed = Speed()

    def render(self):
        print self.position
        
    def horizontal_aceleration(self):
        self.speed.horizontal_aceleration()
        
    def horizonta_deceleration(self):
        self.speed.horizontal_deceleration()
        
    def update(self):
        self.speed.update()
        self.position.x += int(self.speed.velocity.horizontal)
        
    def set_velocity (self, velocity):
        self.speed.aceleration = velocity