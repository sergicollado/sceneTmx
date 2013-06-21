from velocity import *

class PhysicalObject:
    def __init__(self):
        self.velocity = Velocity()
        self.maxim_velocity = 20
        self.friction_reduction = 0.8
        self.aceleration = 10
        
    def vertical_aceleration(self):
        self.velocity.vertical += self.aceleration
        
    def vertical_deceleration(self):
        self.velocity.vertical -= self.aceleration
         
    def horizontal_aceleration(self):
        self.velocity.horizontal += self.aceleration
        
        
    def horizontal_deceleration(self):
        self.velocity.horizontal -= self.aceleration
        
    def reset(self):
        self.velocity.vertical = 0
        self.velocity.horizontal = 0
        
    def update(self,dt):
        self._reduce_vertical_speed(dt)
        self._reduce_horizontal_speed(dt)
     
    def _reduce_vertical_speed(self,dt):
        if(abs(self.velocity.vertical) > 0):
            self.velocity.vertical *= self.friction_reduction*dt
         
    def _reduce_horizontal_speed(self,dt):
        if(abs(self.velocity.horizontal) > 0):
            self.velocity.horizontal *= self.friction_reduction *dt

    def __str__(self):
        return 'velocity: '+self.velocity+' maxim_velocity: '+self.maxim_velocity+ ' aceleraction: '+self.aceleration