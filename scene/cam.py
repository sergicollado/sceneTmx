import data_types
import helpers

class Camera:
    def __init__(self, position):
        self.position = position
        self.speed = helpers.Speed()
        
    def get_position(self):
        return self.position
    
    def panning_right(self):
        self.speed.vertical_aceleration()
        
    def panning_left(self):
        self.speed.vertical_deceleration()

    def panning_top(self):
        self.speed.horizontal_aceleration() 

    def panning_down(self):
        self.speed.horizontal_deceleration()
        
    def update(self):
        self.position.x += int(self.speed.velocity.vertical)
        self.position.y += int(self.speed.velocity.horizontal)
        self.speed.update()

    
    def __str__(self):
        return 'position: '+ str(self.position.x)+',' +str(self.position.y)+' speed: '+ str(self.speed.velocity.vertical)+','+str(self.speed.velocity.horizontal) 