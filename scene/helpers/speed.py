from velocity import *

class Speed:
    def __init__(self):
        self.velocity = Velocity()
        self.maxim_velocity = 2 
        self.friction_reduction = 0.8
        self.aceleration = 2
        
    def vertical_aceleration(self):
        self.velocity.vertical += self.aceleration
        
    def vertical_deceleration(self):
        self.velocity.vertical -= self.aceleration
         
    def horizontal_aceleration(self):
        self.velocity.horizontal += self.aceleration
        
        
    def horizontal_deceleration(self):
        self.velocity.horizontal -= self.aceleration
        
        
    def update(self):
        self.reduce_vertical_speed()
        self.reduce_horizontal_speed()
     
    def reduce_vertical_speed(self):
        if(abs(self.velocity.vertical) > 0):
            self.velocity.vertical *= self.friction_reduction
         
    def reduce_horizontal_speed(self):
        if(abs(self.velocity.horizontal) > 0):
            self.velocity.horizontal *= self.friction_reduction 

    def __str__(self):
        return 'velocity: '+self.velocity+' maxim_velocity: '+self.maxim_velocity+ ' aceleraction: '+self.aceleration