import data_types

class Camara:
    def __init__(self, position):
        self.x = position.x
        self.y = position.y
        self.max_velocity = 2
        self.speed_vertical = 0
        self.speed_horizontal = 0
        self.friction_reduction = 0.8
        
    def get_position(self):
        return data_types.Position(self.x, self.y)
    
    def panning_right(self):
        self.speed_vertical += self.max_velocity 

    def panning_left(self):
        self.speed_vertical -= self.max_velocity

    def panning_top(self):
        self.speed_horizontal += self.max_velocity 

    def panning_down(self):
        self.speed_horizontal -= self.max_velocity
        
    def update(self):
        self.x += self.speed_vertical
        self.y += self.speed_horizontal
        
        self.speed_vertical = self.reduce_speed(self.speed_vertical)
        self.speed_horizontal = self.reduce_speed(self.speed_horizontal)
            
    def reduce_speed(self, speed ):
        if(abs(speed) > 0):
            speed *= self.friction_reduction
        
        return speed