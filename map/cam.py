import data_types

class Camera:
    def __init__(self, position):
        self.position = position
        self.speed = Speed()
        
    def get_position(self):
        return self.position
    
    def panning_right(self):
        self.speed.vertical_aceleration()
        
    def panning_left(self):
        self.speed.vertical_decceletarion()

    def panning_top(self):
        self.speed.horizontal_aceleration() 

    def panning_down(self):
        self.speed.horizontal_deceleration()
        
    def update(self):
        self.position.x += self.speed.velocity.vertical
        self.position.y += self.speed.velocity.horizontal
        self.speed.update()


class Velocity:
    def __init__(self, vertical = 0, horizontal = 0):
        self.vertical = vertical
        self.horizontal = horizontal

class Speed:
    def __init__(self):
        self.velocity = Velocity()
        self.maxim_velocity = 2 
        self.friction_reduction = 0.8
        self.aceleration = 2
        
    def vertical_aceleration(self):
        self.velocity.vertical += self.aceleration

    def vertical_decceletarion(self):
        self.velocity.vertical -= self.aceleration
        
    def horizontal_aceleration(self):
        self.velocity.horizontal += self.aceleration
        
        
    def horizontal_deceleration(self):
        self.velocity.horizontal -= self.aceleration
        
        
    def update(self):
        self.reduce_vertical_speed()
        self.reduce_vertical_speed()
     
    def reduce_vertical_speed(self):
        if(abs(self.velocity.vertical) > 0):
            self.velocity.vertical *= self.friction_reduction
         
    def reduce_horizontal_speed(self):
        if(abs(self.velocity.horizontal) > 0):
            self.velocity.horizontal *= self.friction_reduction

    