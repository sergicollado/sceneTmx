import data_types

class Camara:
    def __init__(self, position):
        self.x = position.x
        self.y = position.y
        self.max_velocity = 2
        self.speed = 0
        self.friction_reduction = 0.8
        
    def get_position(self):
        return data_types.Position(self.x, self.y)
    
    def panning_right(self):
        self.speed += self.max_velocity 

    def panning_left(self):
        self.speed -= self.max_velocity
        
    def update(self):
        self.x += self.speed
        
        if(abs(self.speed) > 0):
            self.speed *= self.friction_reduction